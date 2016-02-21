/* Dropdown Button */
.dropbtn {
    background-color: #7f3939;
    color: #b3b1c5;
    text-align: center;
    text-transform: uppercase;
    padding: 15px;
    font-size: 16px;
    border: none;
    cursor: pointer;
    width: 150px;
}

/* Dropdown button on hover & focus */
.dropbtn:hover, .dropbtn:focus {
    background-color: #817E9F;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: relative;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #7f3939;
    min-width: 160px;
    box-shadow: none;
}

/* Links inside the dropdown */
.dropdown-content a {
    color: white;
    padding: 12px 16px;
    text-decoration: none;
    display: white;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: #817E9F
}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {
  display:block;
}
