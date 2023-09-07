import streamlit as st
from binarytree import Node, build , tree
from PIL import Image

st.set_page_config(
    page_title="Traversal Algorithms In Trees",
    page_icon=":rocket:"
)

def main():
    # find the DFS algorithms 
    ## adjusting the buttons 

    st.write(  "<div style = 'font-family: monospace; font-size : 30px; background-color : lightgrey;'>🚀 BFS and DFS Traversal Playground</div> " , unsafe_allow_html=True)
    st.write("<div style='border:1px solid black;'> </div>" ,unsafe_allow_html=True)
    st.write("<div style = 'font-family: monospace; font-size : 20px; background-color : white ; padding : 10px ; border: 2px solid black;'> Height Adjustable Binary Tree</div> " , unsafe_allow_html=True)

    check_is_perfect = st.checkbox("Make it a perfect tree")
    isPerfectChecker = False

    # st.sidebar.markdown("Adjust sidebar height")
    if check_is_perfect:
        isPerfectChecker = True

    want_letter = st.checkbox("Make the nodes in letters")
    if want_letter:
        want_letter = True
    st.header("Adjust the height of the tree :")

    tree_height = st.slider("select tree height" , min_value=1 , max_value=5 )
    height_adjustable_binary_tree = tree(height = tree_height , is_perfect=isPerfectChecker , letters=want_letter)
    st.graphviz_chart(height_adjustable_binary_tree.graphviz())

    col1 , col2 , col3 = st.columns(3)
    inorder_algo = height_adjustable_binary_tree.inorder
    # if col1.button("inorder"):
    # st.text(f'The Inorder of the tree is : {inorder_algo}')
    with st.expander("INORDER :" , expanded=False):
        st.text(height_adjustable_binary_tree.inorder)

    preorder_algo = height_adjustable_binary_tree.preorder
    with st.expander("PREORDER :" , expanded=False):
        st.text(height_adjustable_binary_tree.preorder)

    # if col2.button("preorder"):
    # st.text(f'The preorder of the tree is : {preorder_algo}')

    postorder_algo = height_adjustable_binary_tree.postorder
    # if col3.button("postorder"):
    with st.expander("POSTORDER :" , expanded=False):
        st.text(height_adjustable_binary_tree.postorder)

    # st.text(f'The preorder of the tree is : {postorder_algo}')

    # st.text(f'The level order of the tree is : {list(height_adjustable_binary_tree)}')
    with st.expander("LEVEL ORDER :" , expanded=False):
        st.text(list(height_adjustable_binary_tree))
    
    with st.expander("More info :"):
        for i , j in height_adjustable_binary_tree.properties.items():
            if j == False:
                i = i.replace("_", " ")
                st.write(f' {i} : no')
            elif j == True:
                i = i.replace("_", " ")
                if j > 1 :
                    st.write(f'{i} : {j}')
                st.write(f' {i} : yes')
            else:
                st.write(f'{i} is : {j}')



    # creating random tree with adjustable height     
    st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        height: 80% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        height: 80% !important;
      }
    </style>""", unsafe_allow_html=True)



    #create a custom binary tree 
    st.write("<div style='border:1px solid black;'> </div>" ,unsafe_allow_html=True)

    st.write("<div style = 'font-family: monospace; font-size : 20px; background-color : white; padding : 10px ; border: 2px solid black;'> Create Custom Binary Tree </div> " , unsafe_allow_html=True)

    rootNode = st.text_input("enter the root node : ")
    leftNode = st.text_input("enter the left node : ")
    rightNode = st.text_input("enter the right node : ")
    left_right_Node = st.text_input("enter the left right node : ")
    left_left_Node = st.text_input("enter the left left node : ")
    right_left_Node = st.text_input("enter the right left node : ")
    right_right_Node = st.text_input("enter the right right node : ")

    root = Node(rootNode)
    root.left = Node(leftNode)
    root.right = Node(rightNode)

    root.left.right = Node(left_right_Node)
    root.left.left = Node(left_left_Node)

    root.right.left = Node(right_left_Node)
    root.right.right = Node(right_right_Node)

    MakeCustomTreePerfect = False
    if st.checkbox("make it perfect"):
        MakeCustomTreePerfect = True

    if rootNode and  leftNode and  rightNode and  left_left_Node and left_right_Node  != type(str) :
        st.graphviz_chart(root.graphviz())
        with st.expander("custom level order"):
            st.text(f'level order : {root.values}')
        with st.expander("custom preorder:"):
            Custom_PreOrder = root.preorder
            st.text(f'custom preorder : {Custom_PreOrder}') 
        with st.expander("custom postorder"):
            Custom_PostOrder = root.postorder
            st.text(f'custom preorder : {Custom_PostOrder}') 
        
    else:
        st.warning("Can't display the tree as you have left fields empty!") 
    
    st.info('want to add more features let me know! mail : shadmanforreal45@gmail.com\n And also graphs dfs and bfs will be added soon!')
    # convert level order to bfs
    st.write("<div style = 'font-family : monospace ; font-size : 30px ; text-align : center'> Please provide your valuable feedback : <a href='http://localhost:8501/'> Link </a> </div>" , unsafe_allow_html=True)

    markdown_text = f"""
    <script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="shadmanshaikh" data-description="Support me on Buy me a coffee!" data-message="" data-color="#5F7FFF" data-position="Right" data-x_margin="18" data-y_margin="18"></script>
    """
    from streamlit.components.v1 import html

    html(markdown_text)



if __name__ == "__main__":
    main()
