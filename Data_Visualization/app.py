import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load dữ liệu
data = pd.read_csv('dataset.csv')  # Đảm bảo đường dẫn đến file là chính xác

# Tạo ứng dụng Dash
app = dash.Dash(__name__)

# Thiết lập layout cho ứng dụng
app.layout = html.Div([
    html.H1("Sales Dashboard"),

    html.Label("Select Year:"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in sorted(data['year'].unique())],
        value=sorted(data['year'].unique()),
        multi=True
    ),

    html.Label("Select Category:"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': category, 'value': category} for category in data['category'].unique()],
        value=data['category'].unique(),
        multi=True
    ),

    dcc.Graph(id='sales-graph')
])

# Callback để cập nhật biểu đồ
@app.callback(
    Output('sales-graph', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('category-dropdown', 'value')]
)
def update_graph(selected_years, selected_categories):
    filtered_data = data[data['year'].isin(selected_years) & data['category'].isin(selected_categories)]
    sales_by_region = filtered_data.groupby('state').sales.sum().reset_index()

    # Tạo biểu đồ hình tròn
    fig = px.pie(sales_by_region, values='sales', names='state', title='Sales by Region')
    return fig

# Chạy ứng dụng
if __name__ == '__main__':
    app.run_server(debug=True)