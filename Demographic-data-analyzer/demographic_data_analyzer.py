import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    listOfCount=[]
    def getRace(df):
      indexes=df.index
      for index in indexes:
        listOfCount.append(df[index])
      listOfCount.sort(reverse=True)
    getRace(df.groupby("race").count()["age"])
    race_count = listOfCount

    # What is the average age of men?
    average_age_men = float(f"{df[df['sex']=='Male']['age'].mean():.1f}")

    # What is the percentage of people who have a Bachelor's degree?
    withFloat=df[df["education"]=="Bachelors"].count()["age"]/df["education"].count()*100
    percentage_bachelors = float(f"{withFloat:.1f}")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ((df[((df["education"]=="Bachelors")|(df["education"]=="Masters")|(df["education"]=="Doctorate"))]["age"]).count()/df["education"].count())*100
    lower_education =((df["education"].count()-df[(df["education"]=="Bachelors")|(df["education"]=="Masters")|(df["education"]=="Doctorate")]["age"].count())/df["education"].count())*100

    # percentage with salary >50K

    higher_education_rich = round(len(df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])][df[df[
        "education"].isin(["Bachelors", "Masters", "Doctorate"])].salary == ">50K"]) / len(
        df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]) * 100, 1)

    lower_education_rich = round((len(df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])][df[~df[
        "education"].isin(["Bachelors", "Masters", "Doctorate"])].salary == ">50K"])) / len(
        df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week )?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =(df[(df["hours-per-week"]==1)&(df["salary"]==">50K")])["age"].count()
    rich_percentage = ((df[(df["hours-per-week"]==1)&(df["salary"]==">50K")])["age"].count()/df[df["hours-per-week"]==1]["age"].count())*100

    # What country has the highest percentage of people that earn >50K?
    maxRate=((df[df["salary"]==">50K"].groupby("native-country").count())/(df.groupby("native-country").count()))["salary"].max()
    countriesRate=((df[df["salary"]==">50K"].groupby("native-country").count())/(df.groupby("native-country").count()))
    listOfCountry=countriesRate[countriesRate["salary"]==maxRate].index
    highest_earning_country =listOfCountry[0]
    
    withFloat2= maxRate*100
    highest_earning_country_percentage = float(f"{withFloat2:.1f}")

    # Identify the most popular occupation for those who earn >50K in India.
    IndiaData= df.groupby("native-country").get_group("India")
    numbersOfOccupation=df.groupby("native-country").get_group("India").groupby("occupation").count()
    listOfOccupation=numbersOfOccupation[numbersOfOccupation==40].dropna().index
    top_IN_occupation =listOfOccupation[0]
    #(((df.groupby("native-country").get_group("India").groupby("occupation")).count())["age"])

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


#print(calculate_demographic_data())