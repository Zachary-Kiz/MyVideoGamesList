import './Login.css'
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button';
import login from '../../api/login';
import { useAuthContext } from '../../../context/AuthContext';

function Login() {

    const {refreshAccessToken} = useAuthContext()

    const submitForm = (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const payload = Object.fromEntries(formData)
        
        login(payload)
        refreshAccessToken()
    }

    return (
        <div className="register_container">
            <form onSubmit={submitForm}>
                <div className='register_content'>
                    <h1>Login</h1>
                    <Input name={"username_or_email"} placeholder={"Email / Username"} />
                    <Input name={"password"} placeholder="Password"/>
                    <Button>Login</Button>
                </div>
            </form>
        </div>
    )
}

export default Login;