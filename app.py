# data_visualizer.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Data Visualizer")

# Sidebar for user inputs
st.sidebar.header("Upload Your Dataset")

# Function to load dataset
def load_data():
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    else:
        st.sidebar.warning("Please upload a CSV file.")
        return None

# Function to create plot
def create_plot(data, plot_type, x_var, y_var, color_var, size_var, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    
    if plot_type == "Scatter Plot":
        sns.scatterplot(data=data, x=x_var, y=y_var, hue=color_var, size=size_var)
    elif plot_type == "Line Chart":
        sns.lineplot(data=data, x=x_var, y=y_var, hue=color_var)
    elif plot_type == "Bar Chart":
        sns.barplot(data=data, x=x_var, y=y_var, hue=color_var)
    elif plot_type == "Histogram":
        sns.histplot(data=data, x=x_var, hue=color_var, multiple="stack")
    elif plot_type == "Box Plot":
        sns.boxplot(data=data, x=x_var, y=y_var, hue=color_var)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    st.pyplot(plt)

# Load dataset
data = load_data()

if data is not None:
    st.write("Dataset Preview")
    st.write(data.head())
    
    # Select plot type
    plot_type = st.sidebar.selectbox("Select Plot Type", ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot"])
    
    # Select variables for the plot
    x_var = st.sidebar.selectbox("Select X-axis Variable", data.columns)
    y_var = st.sidebar.selectbox("Select Y-axis Variable", data.columns, index=1)
    color_var = st.sidebar.selectbox("Select Color Variable", [None] + list(data.columns))
    size_var = st.sidebar.selectbox("Select Size Variable", [None] + list(data.columns))
    
    # Customize plot
    title = st.sidebar.text_input("Plot Title", "My Plot")
    xlabel = st.sidebar.text_input("X-axis Label", x_var)
    ylabel = st.sidebar.text_input("Y-axis Label", y_var)
    
    # Create and display the plot
    create_plot(data, plot_type, x_var, y_var, color_var, size_var, title, xlabel, ylabel)
    
    # Option to download the plot
    if st.sidebar.button("Download Plot"):
        plt.savefig("./Downloads/plot.png")
        st.sidebar.success("Plot saved as plot.png")
else:
    st.warning("Please upload a dataset to start visualizing.")
