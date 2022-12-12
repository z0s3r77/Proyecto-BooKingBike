import os

#Comprobamos si existe el directorio css , sino, lo crea
if not os.path.exists('docs/css/'):
    os.makedirs('docs/css/')


def css():
    print("""@import url(https://fonts.googleapis.com/css?family=Open+Sans);

    body {
    background-color: rgb(252, 206, 106);
    font-family: 'Open Sans',serif;
    }

    h1 {
    padding-left: 30px;
    color: #005763;
    font-size: 39px;
    }

    h2 {
    padding-left: 30px;
    color: #005763;
    }

    /* BARRA DE NAVEGACIÓN */
    nav {
    position: sticky;
    top: 0;
    z-index: 1;
    margin-top: 35px;
    margin-bottom: 20px;
    display: block;
    }

    ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: rgb(168, 125, 46);
    }

    li {
    float: left;
    }

    li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    }

    li a:hover:not(.active) {
    background-color: rgb(182, 131, 35);
    }

    .active {
    background-color: #006977;
    }

    .active2 {
    background-color: #017888ce;
    }

    a.titulo {
    color: rgb(182, 131, 35);
    font-size: 20px;
    text-decoration: underline;
    }


    li.dropdown {
    display: inline-block;
    }

    .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px #006977;
    ;
    z-index: 1;
    }

    .dropdown-content a {
    color: #006977;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
    }

    .dropdown-content a:hover {
    background-color: #f1f1f1;
    }

    .dropdown:hover .dropdown-content {
    display: block;
    }

    /* FIN Barra de Navegacion */


    /* CONTENEDORES FLEX */

    .flex-container {
    display: flex;
    flex-wrap: wrap;
    background-color: rgb(255, 204, 93);
    }

    div.container {
    position: relative;
    background-color: #007a8a;
    width: 450px;
    height: 225px;
    margin: auto;
    line-height: 75px;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 10px;
    margin-bottom: 10px;
    transition-duration: 1.4s;

    }

    div.container:hover {
    transition-duration: 2;
    cursor: pointer;
    }

    p {
    font-size: 0.9em;
    letter-spacing: 1px;
    }

    .product {
    position: absolute;
    width: 40%;
    top: 3%;
    left: 55%;
    }

    .desc {
    letter-spacing: 0;
    margin-bottom: 10px;
    line-height: 1.1em;
    text-align: justify;
    color: white;
    }

    div.images>img {
    margin-top: 25px;
    margin-left: 40px;
    width: 175px;
    height: 175px;
    }


    div.product>p:first-of-type {
    color: rgb(182, 131, 35);
    font-size: 25px;
    font-weight: bold;
    }


    .button {
    color: white;
    padding: 5px 5px;
    margin-left: 40px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 13px;
    background-color: white;
    color: black;
    border: 3.5px solid rgb(182, 131, 35);
    border-radius: 10px;
    transition-duration: 0.4s;
    cursor: pointer;
    }

    .button:hover {
    background-color: rgb(182, 131, 35);
    color: white;
    }

    div.container-subpage {
    align-items: center;
    display: flex;
    height: 150px;
    justify-content: center;
    width: 300px;
    margin: auto;
    line-height: 75px;
    margin-top: 10px;
    margin-bottom: 10px;
    background: #ffff99;
    border-width: 3px;
    border-style: solid;
    border-radius: 35px;
    font-weight: 600;
    font-size: 40px;
    
    }

    div.container-p {
    text-align: center;
    border: 1px dotted #000;
    }

    /* FIN CONTENEDORES FLEX */


    /* BARRA FOOTER */

    .footer {

    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgb(168, 125, 46);
    color: white;
    text-align: center;
    position: absolute;


    }

    html {
    min-height: 100%;
    position: relative;
    }

    /* Contactp */

    @import url(https://fonts.googleapis.com/css?family=Noto+Sans);




    .contact_form {
    width: 460px;
    height: auto;
    margin: 80px auto;
    border-radius: 10px;
    padding-top: 30px;
    padding-bottom: 20px;
    background-color: #fbfbfb;
    padding-left: 30px;
    }


    input {
    background-color: #fbfbfb;
    width: 408px;
    height: 40px;
    border-radius: 5px;
    border-style: solid;
    border-width: 1px;
    border-color: #ab4493;
    margin-top: 10px;
    padding-left: 10px;
    margin-bottom: 20px;
    }


    textarea {
    background-color: #fbfbfb;
    width: 405px;
    height: 150px;
    border-radius: 5px;
    border-style: solid;
    border-width: 1px;
    border-color: #ab4493;
    margin-top: 10px;
    padding-left: 10px;
    margin-bottom: 20px;
    padding-top: 15px;
    }


    label {
    display: block;
    float: center;
    }


    button {
    height: 45px;
    padding-left: 5px;
    padding-right: 5px;
    margin-bottom: 20px;
    margin-top: 10px;
    text-transform: uppercase;
    background-color: #ab4493;
    border-color: #ab4493;
    border-style: solid;
    border-radius: 10px;
    width: 420px;
    cursor: pointer;
    }


    button p {
    color: #fff;
    }


    span {
    color: #ab4493;
    }


    .aviso {
    font-size: 13px;
    color: #0e0e0e;
    }




    h3 {
    font-size: 16px;
    padding-bottom: 30px;
    color: #0e0e0e;
    }




    ::-webkit-input-placeholder {
    color: #a8a8a8;
    }


    ::-webkit-textarea-placeholder {
    color: #a8a8a8;
    }


    .formulario input:focus {
    outline: 0;
    border: 1px solid #97d848;
    }


    .formulario textarea:focus {
    outline: 0;
    border: 1px solid #97d848;
    }


    /* Links */

    a{
    text-decoration:none;
    }

    p a:visited {
    color: #006977;
    }


    p a:link {
    color: rgb(168, 125, 46);

    }

    p a{
    border: solid 3px white;
    background-color: wheat;
    padding-left: 40px;
    padding-right: 40px;
    padding-top: 20px;
    padding-bottom: 20px;
    }


    /* table */


    table {
    width: 100%;
    margin-top: 20px;
    border: solid 5px black;
    }

    th, td {
    text-align: center;
    padding: 8px;
    }

    tr:nth-child(even){background-color: #f2f2f2}

    th {
    background-color:  rgb(168, 125, 46);
    color: white;
    }


    /* home */





    .responsive {
    width: 100%;
    height: auto;
    max-width: 1400px;
    }

    .header{
    width: 100%;
    height: auto;
    }

    .response-p {
    justify-content: center;
    background-color: wheat;
    max-width: 1800px;
    font-size: 1.2rem;
    }

    .specifications{
    font-size: 1.5em;
    }

    .specifications-group{
    margin-top: 20px;
    background-color: rgb(61, 171, 222);
    margin-bottom: 220px;
    margin-right: 320px;
    border: solid 3px black;
    min-width: 400px;
    }



    button.sale {
    background-color:rgb(168, 125, 46); /* Green */
    border: none;
    color: white;
    padding: 15px 30px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
    color:rgb(61, 171, 222);
    width:320px;
    }

    button.sale:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
    }

    .responsive-sale {
    width: 100%;
    height: auto;
    max-width: 700px;
    min-width: 150px;

    }

    button a:visited{
    color: #006977;
    font-weight: bold;
    }
    
    button a:link {
        color: rgb(24, 16, 1);
        font-weight: bold;
    
    }""")