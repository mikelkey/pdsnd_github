"""
This bikeshare program compiles data about a bikesharing organization with locations
in 3 different cities. Chicago, New York City, and Washington.
Based on user input, it loads data from .csv files, filters the data based on
the input and provides statistical computations about the data.
"""

import time
import pandas as pd

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

    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to search? Chicago, New York City, or Washington:\n').lower()
        city_list = ['chicago', 'new york city', 'washington']
        if city in city_list:
            break
        else:
            print('\nPlease enter a valid city name\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to search? January, February, March, April, May, June or all:\n').lower()
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in month_list:
            break
        else:
            print('\nPlease enter a valid month or enter "all"')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to search? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all:\n').lower()
        day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day in day_list:
            break
        else:
            print('\nPlease enter a valid day or enter "all"\n')
    print('-'*30)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data from .csv file based on user input. Applies filters for "all".
    Then asks the user for input if the user would like to view the data, 5 rows
    at a time.
    """

    # Load csv file with user input
    df = pd.read_csv(CITY_DATA[city])

    # Add columns to table
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.day_name()
    df['hour']= df['Start Time'].dt.hour
    df['time']= df['Start Time'].dt.time

    # Applying filters for 'all'
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        df = df[df['month'] == month]
    if day.lower() != 'all':
        df = df[df['day'] == day.title()]

    # Asks user if they would like to view data
    start_loc = 0
    view_data = input ('\nWould you like to view the data (5 rows at a time)? Type "Yes" or "No"\n').lower()
    while True:
        if view_data == 'yes':
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
            view_data = input('\nWould you like to view more data (5 rows at a time)? Type "Yes" or "No"\n').lower()
        elif view_data == 'no':
            break
        else:
            print('\nPlease enter a valid input\n')
            view_data = input ('\nWould you like to view the data (5 rows at a time)? Type "Yes" or "No"\n').lower()

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:\n{}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('The most common day of the week is:\n{}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is:\n{}'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*30)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:\n{}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is:\n{}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + (' to ') + df['End Station']
    print('The most common trip is:\n{}'.format((df['combo'].mode()[0])))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*30)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_trip_duration = df['Trip Duration'].sum()/60/60
    print('The total travel time is:\n{} hours'.format(sum_trip_duration))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('The average travel time is:\n{} minutes'.format(mean_travel_time))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*30)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Information about users:\n{}/n'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('\nThe gender count is:\n{}'.format(gender_count))
    else:
        print('Gender count information is unavailable for this city/n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob = df['Birth Year'].min()
        print('\nThe earliest birth year is:\n{}'.format(earliest_yob))
        most_recent_yob = df['Birth Year'].max()
        print('The most recent year of birth is:\n{}'.format(most_recent_yob))
        common_yob = df['Birth Year'].mode().values[0]
        print('The most common birth year is:\n{}'.format(common_yob))
    else:
        print('Earliest, most recent, and most common year of birth information is unavailable for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*30)

def main():
    """
    Applies functions while user is in program. Allows the user to either exit
    or perform a new search.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to perform a new search? Enter "Yes" or "No".\n').lower()
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
