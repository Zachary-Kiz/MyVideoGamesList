import './Input.css'

function Input({placeholder, minText}) {
    return (
        <div className='mvgl_input_container'>
            <input name={placeholder} placeholder={placeholder} className="mvgl_input"></input>
            {minText && <small>{minText}</small>}
        </div>
)
}

export default Input;