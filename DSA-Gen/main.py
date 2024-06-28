import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from LLM import analyze_complexity

def plot_complexity_graph(complexity, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    n = np.arange(1, 101)
    
    if complexity == 'O(1)':
        y = np.ones_like(n)
    elif complexity == 'O(log n)':
        y = np.log2(n)
    elif complexity == 'O(n)':
        y = n
    elif complexity == 'O(n log n)':
        y = n * np.log2(n)
    elif complexity == 'O(n^2)':
        y = n ** 2
    elif complexity == 'O(n^3)':
        y = n ** 3
    elif complexity == 'O(2^n)':
        y = 2 ** np.minimum(n, 30)   
    elif complexity.lower() == 'o(n!)':
        y = np.array([np.math.factorial(min(i, 20)) for i in n])  
    else:
        y = n  

    ax.plot(n, y)
    ax.set_title(f'{title} - {complexity}')
    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Complexity')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.grid(True)
    ax.set_ylim(bottom=1)   
    st.pyplot(fig)

def main():
    st.set_page_config(layout="wide")
    st.title('Time and Space Complexity Analysis GenAi')
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Code Input")
        code = st.text_area("Enter your code here:", height=300)
        
        if st.button("Analyze"):
            if code:
                try:
                    analysis = analyze_complexity(code)
                    time_complexity, space_complexity, explanation = analysis.split('\n', 2)
                    
                    time_complexity = time_complexity.split(': ')[1]
                    space_complexity = space_complexity.split(': ')[1]
                    
                    st.session_state.time_complexity = time_complexity
                    st.session_state.space_complexity = space_complexity
                    st.session_state.explanation = explanation.strip()
                except Exception as e:
                    st.error(f"Error analyzing code: {str(e)}")
            else:
                st.warning("Please enter some code to analyze.")
    
    with col2:
        if 'time_complexity' in st.session_state and 'space_complexity' in st.session_state:
            st.header("Complexity Analysis")
            
            st.subheader("Time Complexity")
            plot_complexity_graph(st.session_state.time_complexity, "Time Complexity")
            
            st.subheader("Space Complexity")
            plot_complexity_graph(st.session_state.space_complexity, "Space Complexity")
            
            st.subheader("Explanation")
            st.write(st.session_state.explanation)

if __name__ == '__main__':
    main()