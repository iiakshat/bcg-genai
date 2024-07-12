import streamlit as st
import pandas as pd


def remove_commas(value):
    value = value.split(',')
    value = ''.join(value)
    return int(value)

def input_data():
    df = pd.read_csv("10K.csv")
    for col in df.columns:
        if col not in ["Company", "Year"]:
            df[col] = df[col].map(remove_commas)
    df = df.sort_values(['Company','Year'],ascending=True).groupby('Company').head()
    return df

def revenue_check(df):
    df_revenue = pd.DataFrame(columns=['Company','Year','Total Revenue','Revenue Growth (%)'])
    df_revenue['Company'] = df['Company']
    df_revenue['Year'] = df['Year']
    df_revenue['Total Revenue'] = df['Total Revenue']
    df_revenue['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
    return df_revenue

def assets_check(df):
    df_assets = pd.DataFrame(columns=['Company','Year','Total Assets','Total Assets Growth (%)'])
    df_assets['Company'] = df['Company']
    df_assets['Year'] = df['Year']
    df_assets['Total Assets'] = df['Total Assets']
    df_assets['Total Assets Growth (%)'] = df.groupby(['Company'])['Total Assets'].pct_change() * 100
    return df_assets

def income_check(df):
    df_income = pd.DataFrame(columns=['Company','Year','Net Income','Net Income Growth (%)'])
    df_income['Company'] = df['Company']
    df_income['Year'] = df['Year']
    df_income['Net Income'] = df['Net Income']
    df_income['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100
    return df_income

def liability_check(df):
    df_liability = pd.DataFrame(columns=['Company','Year','Total Liabilities','Total Liabilities Growth (%)'])
    df_liability['Company'] = df['Company']
    df_liability['Year'] = df['Year']
    df_liability['Total Liabilities'] = df['Total Liabilities']
    df_liability['Total Liabilities Growth (%)'] = df.groupby(['Company'])['Total Liabilities'].pct_change() * 100
    return df_liability

def cashflow_check(df):
    df_cashflow = pd.DataFrame(columns=['Company','Year','Cash Flow','Cash Flow Growth (%)'])
    df_cashflow['Company'] = df['Company']
    df_cashflow['Year'] = df['Year']
    df_cashflow['Cash Flow'] = df['Cash Flow']
    df_cashflow['Cash Flow Growth (%)'] = df.groupby(['Company'])['Cash Flow'].pct_change() * 100
    return df_cashflow

def main():
    df = input_data()
    st.title("Financial Chat Bot")
    chatbox = st.container(height=300, border=True)
    prompt = chatbox.chat_input("Say something", key="chat-input")
    if prompt:
        if prompt.lower().find("revenue of apple in 2022") != -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][7]
            chatbox.write(f"Total Revenue of Apple in the Year 2022 was ${(format (value, ',d'))}")
        if prompt.lower().find("revenue of apple in 2021") != -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][6]
            chatbox.write(f"Total Revenue of Apple in the Year 2021 was ${(format (value, ',d'))}")
        if prompt.lower().find("revenue of apple") != -1 and prompt.lower().find("2022") == -1 and prompt.lower().find("2021") == -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][8]
            chatbox.write(f"Total Revenue of Apple in the Year 2023 was ${(format (value, ',d'))}")

        if prompt.lower().find("revenue of microsoft in 2022") != -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][1]
            chatbox.write(f"Total Revenue of Microsoft in the Year 2022 was ${(format (value, ',d'))}")
        if prompt.lower().find("revenue of microsoft in 2021") != -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][2]
            chatbox.write(f"Total Revenue of Microsoft in the Year 2021 was ${(format (value, ',d'))}")
        if prompt.lower().find("revenue of microsoft") != -1 and prompt.lower().find("2022") == -1 and prompt.lower().find("2021") == -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][0]
            chatbox.write(f"Total Revenue of Microsoft in the Year 2023 was ${(format (value, ',d'))}")

        if prompt.lower().find("revenue of tesla in 2022") != -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][4]
            chatbox.write(f"Total Revenue of Tesla in the Year 2022 was ${(format (value, ',d'))}")
        if prompt.lower().find("revenue of tesla in 2021") != -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][5]
            chatbox.write(f"Total Revenue of Tesla in the Year 2021 was ${(format (value, ',d'))}")
        if prompt.lower().find("revenue of tesla") != -1 and prompt.lower().find("2022") == -1 and prompt.lower().find("2021") == -1:
            df_revenue = revenue_check(df)
            value = df_revenue['Total Revenue'][3]
            chatbox.write(f"Total Revenue of Tesla in the Year 2023 was ${(format (value, ',d'))}")

        if prompt.lower().find("income changed for") != -1 or prompt.lower().find("change in income for") != -1:
            company_name = prompt.split('for')[1].strip().lower()
            if company_name == 'apple':
                index = 6
            if company_name == 'microsoft':
                index = 0
            if company_name == 'tesla':
                index = 3
            df_income = income_check(df)
            change = df_income['Net Income Growth (%)'][index]
            print(df_income['Net Income Growth (%)'])
            if change < 0:
                chatbox.write(f"The revenue has decreased for {company_name.capitalize()} in the year 2023 by about {round(change,2)}%")
            else:
                chatbox.write(f"The revenue has increased for {company_name.capitalize()} in the year 2023 by about {round(change,2)}%")
        else:
            chatbox.write(f"Sorry, I can only provide information on predefined queries.")


if __name__ == "__main__":
    main()

    