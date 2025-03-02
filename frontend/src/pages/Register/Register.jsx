import './Register.css'
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button';
import createUser from '../../api/createUser'

function Register() {

    const submitForm = (e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const payload = Object.fromEntries(formData)
        delete payload['password2']
        createUser(payload)
    }

    return (
        <div className="register_container">
            <form onSubmit={submitForm}>
                <div className='register_content'>
                    <h1>Register</h1>
                    <Input name={"username"} placeholder={"Username"}></Input>
                    <Input name={"email"} placeholder={"Email"} />
                    <Input name={"password"} placeholder="Password"/>
                    <Input name={"password2"} placeholder="Re-enter Password"/>
                    <Button>Register</Button>
                </div>
            </form>
        </div>
    )
}

export default Register;