import pandas as pd
import plotly.express as px

# Load the data (replace with your actual data loading method)
data = {
    'country': ['Finland', 'Denmark', 'Iceland', 'Sweden', 'Israel', 'Netherlands', 'Norway', 'Luxembourg',
                'Switzerland', 'Australia', 'New Zealand', 'Costa Rica', 'Kuwait', 'Austria', 'Canada',
                'Belgium', 'Ireland', 'Czech Republic', 'Lithuania', 'United Kingdom', 'Slovenia',
                'United Arab Emirates', 'United States', 'Germany', 'Mexico', 'Uruguay', 'France',
                'Saudi Arabia', 'Singapore', 'Taiwan', 'Romania', 'El Salvador', 'Estonia', 'Poland',
                'Spain', 'Serbia', 'Chile', 'Panama', 'Malta', 'Italy', 'Guatemala', 'Nicaragua',
                'Brazil', 'Slovakia', 'Latvia', 'Uzbekistan', 'Argentina', 'Kazakhstan', 'Cyprus', 'Japan',
                'South Korea', 'Philippines', 'Vietnam', 'Portugal', 'Hungary', 'Paraguay', 'Thailand',
                'Malaysia', 'China', 'Honduras', 'Bahrain', 'Croatia', 'Greece', 'Bosnia and Herzegovina',
                'Libya', 'Jamaica', 'Peru', 'Dominican Republic', 'Mauritius', 'Moldova', 'Russia', 'Bolivia',
                'Ecuador', 'Montenegro', 'Mongolia', 'Colombia', 'Venezuela', 'Indonesia', 'Bulgaria',
                'Armenia', 'South Africa', 'North Macedonia', 'Algeria', 'Hong Kong', 'Albania', 'Tajikistan',
                'Republic of the Congo', 'Mozambique', 'Georgia', 'Iraq', 'Nepal', 'Laos', 'Gabon',
                'Ivory Coast', 'Guinea', 'Turkey', 'Senegal', 'Iran', 'Azerbaijan', 'Nigeria', 'Palestine',
                'Cameroon', 'Ukraine', 'Namibia', 'Morocco', 'Pakistan', 'Niger', 'Burkina Faso',
                'Mauritania', 'Gambia', 'Chad', 'Kenya', 'Tunisia', 'Benin', 'Uganda', 'Myanmar',
                'Cambodia', 'Ghana', 'Liberia', 'Mali', 'Madagascar', 'Togo', 'Jordan', 'India',
                'Egypt', 'Sri Lanka', 'Bangladesh', 'Ethiopia', 'Tanzania', 'Comoros', 'Yemen', 'Zambia',
                'Eswatini', 'Malawi', 'Botswana', 'Zimbabwe', 'DR Congo', 'Sierra Leone', 'Lesotho',
                'Lebanon', 'Afghanistan', 'Turkmenistan', 'Rwanda', 'Kyrgyzstan', 'Belarus'],
    'happiness_score': [7.74, 7.58, 7.53, 7.34, 7.34, 7.32, 7.30, 7.12, 7.06, 7.06, 7.03, 6.96, 6.95, 6.91,
                          6.90, 6.89, 6.84, 6.82, 6.82, 6.75, 6.74, 6.73, 6.73, 6.72, 6.68, 6.61, 6.61,
                          6.59, 6.52, 6.50, 6.49, 6.47, 6.45, 6.44, 6.42, 6.41, 6.36, 6.36, 6.35, 6.32,
                          6.29, 6.28, 6.27, 6.26, 6.23, 6.20, 6.19, 6.19, 6.07, 6.06, 6.06, 6.05, 6.04,
                          6.03, 6.02, 5.98, 5.98, 5.98, 5.97, 5.97, 5.96, 5.94, 5.93, 5.88, 5.87, 5.84,
                          5.84, 5.82, 5.82, 5.82, 5.79, 5.78, 5.73, 5.71, 5.70, 5.70, 5.61, 5.57, 5.46,
                          5.46, 5.42, 5.37, 5.36, 5.32, 5.30, 5.28, 5.22, 5.22, 5.19, 5.17, 5.16, 5.14,
                          5.11, 5.08, 5.02, 4.98, 4.97, 4.92, 4.89, 4.88, 4.88, 4.87, 4.87, 4.83, 4.80,
                          4.66, 4.56, 4.55, 4.51, 4.49, 4.47, 4.47, 4.42, 4.38, 4.37, 4.35, 4.34, 4.29,
                          4.27, 4.23, 4.23, 4.21, 4.19, 4.05, 3.98, 3.90, 3.89, 3.86, 3.78, 3.57, 3.56,
                          3.50, 3.50, 3.42, 3.38, 3.34, 3.30, 3.25, 3.19, 2.71, 1.72, None, None, None, None]
}

df = pd.DataFrame(data)

# Handle missing data:  Replace 'No Data' with NaN and then drop rows with NaN in 'happiness_score'
df['happiness_score'] = pd.to_numeric(df['happiness_score'], errors='coerce')  # Convert to numeric, forcing errors to NaN
df = df.dropna(subset=['happiness_score']) # Remove rows where happiness_score is NaN

# Create the choropleth map
fig = px.choropleth(df,
                    locations="country",
                    locationmode='country names',  # Use 'country names' for accurate matching
                    color="happiness_score",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma,  # Choose a color scale
                    title="World Happiness Report 2024")

fig.show()