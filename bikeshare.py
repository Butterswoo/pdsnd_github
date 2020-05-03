import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_input = input('Please input the name of the city to analyze: ').lower()
        if city_input in CITY_DATA:
            city = city_input
            break
        else:
            print('Enter a valid city!(chicago, new york city, washington)')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_input = input('Please input the month to filter by, or "all" to apply no month filter: ').lower()
        if month_input in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = month_input
            break
        else:
            print('Enter a valid month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input('Please input the day of week: (all, monday, tuesday, ... sunday) ').lower()
        if day_input in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = day_input
            break
        else:
            print('Enter a valid day of week!')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day of week'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day of week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day of week'].mode()[0]
    print('Most Popular day of week:', popular_day_of_week)
    
    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Stations: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Popular End Stations: ', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['startend'] = df['Start Station'] +'--' + df['End Station']
    start_end = df['startend'].mode()[0]
    print('Most Popular Start-End Station combination: ',start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total trip duration: ', total)

    # TO DO: display mean travel time
    avg = df['Trip Duration'].mean()
    print('Average trip duration: ', avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Counts of gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].max()
    print('Earliest year of birth: ', int(earliest))
    recent = df['Birth Year'].min()
    print('Most recent year of birth: ', int(recent))
    common = df['Birth Year'].mode()[0]
    print('Most common year of birth: ', int(common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    while True:    
        answer = input('Would you like to see individual customer data? ').lower()
        i = 0
        if answer == 'no':
            break
        elif answer == 'yes':
            print(df.loc[i:i+4])
            while True:
                i += 5
                answer_2 = input('Would you like to check more data? ').lower()
                if answer_2 == 'no':
                    return
                elif answer_2 == 'yes':
                    print(df.loc[i:i+4])
                else:
                    print('Please enter yes/no')
        else:
            print('Please enter yes/no')
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()