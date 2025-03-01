import './Login.css'
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button'

function Login() {

    const submitForm = (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const payload = Object.fromEntries(formData)

        console.log(payload)
    }

    return (
        <div className="register_container">
            <form onSubmit={submitForm}>
                <div className='register_content'>
                    <h1>Login</h1>
                    <Input placeholder={"Email / Username"} />
                    <Input placeholder="Password"/>
                    <Button>Login</Button>
                </div>
            </form>
        </div>
    )
}

export default Login;