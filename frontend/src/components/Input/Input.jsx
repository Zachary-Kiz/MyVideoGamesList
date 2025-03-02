import './Input.css'

function Input({name,placeholder, minText}) {
    return (
        <div className='mvgl_input_container'>
            <input name={name} placeholder={placeholder} className="mvgl_input"></input>
            {minText && <small>{minText}</small>}
        </div>
    )
}

export default Input;