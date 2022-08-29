import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df.age[df.sex == 'Male'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    total = df.education.count() 
    percentage_bachelors = round(100* df.education[df.education == 'Bachelors'].count() / total, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(100* df.education[((df.education == 'Bachelors') | (df.education =='Masters') | (df.education == 'Doctorate'))].count() / total,1)
    lower_education = round(100* df.education[~((df.education == 'Bachelors') | (df.education =='Masters') | (df.education == 'Doctorate'))].count() / total,1)

    # percentage with salary >50K
    df1 = df[((df.education == 'Bachelors') | (df.education =='Masters') | (df.education == 'Doctorate'))]
    total_high_education = df1.salary.count()
    higher_education_rich = round(100*df1.education[df1.salary == '>50K'].count() / total_high_education, 1)
    
    df2 = df[~((df.education == 'Bachelors') | (df.education =='Masters') | (df.education == 'Doctorate'))]
    total_low_education = (total - total_high_education)
    lower_education_rich = round(100 * df2.salary[df2.salary == '>50K'].count() / total_low_education  ,1)
    lower_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_rich = df[df['hours-per-week'] == df['hours-per-week'].min()].salary.count()
    num_min_workers = df.salary[(df.salary == '>50K') & (df['hours-per-week'] == 1)].count() 
    rich_percentage = round(100 * num_min_workers / total_rich , 1)


    # What country has the highest percentage of people that earn >50K?
    p = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    p.sort_values(ascending=False, inplace=True)
    highest_earning_country = p.head(1).index[0]
    highest_earning_country_percentage = round(100 * p.head(1).values[0], 1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country']=='India') & (df.salary == '>50K')].occupation.value_counts().head(1).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
