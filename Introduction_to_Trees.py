import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector


st.set_page_config(
    page_title="Traversal Algorithms In Trees",
    page_icon=":rocket:"
)

st.write("<div style='font-family: monospace; font-size: 20px ; text-align: center'> About the Project: </div>\n\n" , unsafe_allow_html=True)
st.write("<div style='font-family: monospace; font-size: 20px ; text-align: center'> Practice All Your Major Tree DFS & BFS Algorithms Here! </div>\n\n" , unsafe_allow_html=True)


st.sidebar.header("Introduction Page")
st.write("<div style='border:1px solid black;'> </div>" ,unsafe_allow_html=True)

st.write("<div style='font-family: monospace; font-size: 20px ; text-align: center'> This is a basic Introduction to trees traversal algorithms</div>\n\n" , unsafe_allow_html=True)

st.text("want to skip theory just like you did in your exams or just want to practice!!:")
st.write("<div style='font-family: monospace; font-size: 20px ; text-align: center'> Click the Below Button 👇: </div>\n\n" , unsafe_allow_html=True)
st.write("<div style='font-family: monospace; font-size: 20px ; text-align: center;'><button><a style='color: black; text-decoration: none;' href='playground'>Playground</a></button> </div>\n\n" , unsafe_allow_html=True)


st.write("<div style = 'font-family : monospace ; font-size : 30px ; text-align : center'> Tree Traversal Algorithms  </div>" , unsafe_allow_html=True)
st.write("<div style='font-family: monospace; font-size: 20px ; text-align: center;'> In-order, preorder, postorder, and level order are binary tree traversal techniques. In-order visits nodes in ascending order, while preorder visits the root before its children. Postorder traverses children before the root, and level order visits nodes by levels from left to right. These methods serve different purposes in tree manipulation and data retrieval.</div> " , unsafe_allow_html=True)
postOrderImg = 'src/post_order.gif'
st.image(postOrderImg , caption="Example for Post order Traversal" , use_column_width=True)
st.write("for in-depth explaination on trees visit : [link](https://en.wikipedia.org/wiki/Tree_(data_structure))")


# provide feedback system

st.write("<div style = 'font-family : monospace ; font-size : 30px ;'> Provide Your Valuable Feedback : </div>" , unsafe_allow_html=True)

collector = FeedbackCollector(
    email=st.secrets.TRUBRICS_EMAIL,
    password=st.secrets.TRUBRICS_PASSWORD,
    project="default"
)


print(st.secrets.TRUBRICS_EMAIL)

user_feedback = collector.st_feedback(
    component="default",
    feedback_type="faces",
    open_feedback_label="[Optional] Provide additional feedback",
    align="flex-start",
    model = "Decision Trees",
    single_submit=False
)







# author details
creator_name = "shadman"
github_link = "https://github.com/shadmanshaikh"
linkedin_link = "https://www.linkedin.com/in/shadman-shaikh-xan"




# about the author
footer_html = f"""
<footer style="text-align: center;">
    <p>Created by {creator_name}</p>
    <p>
        <a href="{github_link}" target="_blank">GitHub</a> | 
        <a href="{linkedin_link}" target="_blank">LinkedIn</a>
    </p>
</footer>
"""

# Display the HTML footer using st.markdown
st.markdown(footer_html, unsafe_allow_html=True)
