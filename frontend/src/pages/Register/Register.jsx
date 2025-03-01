import './Register.css'
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button'

function Register() {

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
                    <h1>Register</h1>
                    <Input placeholder={"Username"}></Input>
                    <Input placeholder={"Email"} />
                    <Input placeholder="Password"/>
                    <Input placeholder="Re-enter Password"/>
                    <Button>Register</Button>
                </div>
            </form>
        </div>
    )
}

export default Register;