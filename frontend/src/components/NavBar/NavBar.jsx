import './NavBar.css'

function NavBar() {
    return (
        <div className='mvgl_navbar'>
            <a href='/user/login' className='mvgl_navbar_item'>Log In </a>
            <a href='/user/register' className='mvgl_navbar_item'>Register</a>
        
        </div>
    )
}

export default NavBar;