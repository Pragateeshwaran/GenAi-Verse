from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
)

def analyze_complexity(code):
    
    system = """
    You are a powerful data structure teacher. Analyze the given code and provide the following information: 
    1) Time complexity, 
    2) Space complexity, 
    3) A brief explanation of why the code has these complexities. 
    Format your response as follows: 'Time complexity: O(X)\nSpace complexity: O(Y)\nExplanation: [Your explanation here]'
    """
    
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    res = chain.invoke({"text": code})
    print(res)
    return res.content