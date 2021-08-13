import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')
print('\n please choose a city from the below list by writing down the desired city name!')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyzet
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('chicago | new york city | washington:  ').lower()
        if city not in {'chicago', 'new york city' , 'washington'}:
            print('\nPlease make sure that you chose a city from the mentioned cities')
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\n Enter a month between (january to june) or type "all" to display all months:  ').lower()
        if month not in {'january', 'february' , 'march', 'april', 'may', 'june', 'all'}:
            print('\nPlease make sure that you enter a full valid month name within the mentioned period')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\n Enter a day of the week or type "all" to display the statstics for all days of the week :  ').lower()
        if day not in {'sunday', 'monday' , 'tuesday', 'wednesday', 'thuresday', 'friday', 'saturday', 'all'}:
            print('Please make sure that you enter a full valid day name')
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hours from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent day:', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    start_station = df['Start Station'].mode()[0]
    end_station = df['End Station'].mode()[0]
    Trip = ('FROM ' + df['Start Station'] + ' TO ' + df['End Station']).mode()[0]
    print('Most popular start station:', start_station, '\nMost popular end station:', end_station, '\nMost common trip:', Trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total trip duration:', travel_time, ' seconds')

    # display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('Average trip duration:', avg_travel, ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print('users distribution: ', user_types)

    # Display counts of gender
    if 'Gender' in df:
        Genders = df.groupby(['Gender'])['Gender'].count()
        print('Gender distribution: ', Genders)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        commonb = int(df['Birth Year'].mode()[0])
        print('Earliest birth year is: ', earliest, '\nwhile most recent birth year is: ', recent, '\nHowever, the common birth year is: ', commonb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):

    print('\nDisplying row data...\n')

    start_loc = 0
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()

    while True:
        if view_data == 'no':
            break
        print(df[start_loc:start_loc + 5])
        view_data = input('Do you wish to continue? yes/no: ').lower()
        start_loc += 5


    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
