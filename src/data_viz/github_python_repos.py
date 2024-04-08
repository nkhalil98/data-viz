import requests
import plotly.express as px

API_URL = "https://api.github.com/search/repositories"

query = API_URL + "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(query, headers=headers)

data = response.json()
n_repos = data["total_count"]
complete_results = not data["incomplete_results"]
print(
    f"Queried {n_repos} Python repositories with more than 10,000 stars. Complete results status: {complete_results}."
)

# Extract the names and star counts of the most popular Python repositories
available_repos = data["items"]
links, stars, hover_texts = [], [], []
for repo in available_repos:
    name = repo["name"]
    url = repo["html_url"]
    link = f'<a href="{url}">{name}</a>'
    star_count = repo["stargazers_count"]
    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_text = f"{owner}<br />{description}<br />{url}"
    links.append(link)
    stars.append(star_count)
    hover_texts.append(hover_text)

# Plot the most popular Python repositories
fig = px.bar(
    x=links,
    y=stars,
    labels={"x": "Repository", "y": "Stars"},
    title="Most popular Python repositories on GitHub",
    hover_name=hover_texts,
)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
fig.update_traces(marker_color="SteelBlue", opacity=0.6)
fig.show()
