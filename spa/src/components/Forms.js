import React from 'react'

const TextInput = ({_className, placeholder, name, label, handler}) => {
    return (

        <div>
            <div className="my-1">
                <label>{label ?? "textInputLabel"}</label>
            </div>
            <div>
                <input
                    type="text"
                    name={name ?? "inputName"}
                    placeholder={placeholder ?? ""}
                    onChange={handler}
                    className={_className ?? "h-10 w-full border-1 border"}>
                </input>
            </div>
        </div>
        
    )
}
const PasswordInput = ({_className, placeholder, name, label, handler}) =>{
    return (
        <div>
            <div className="my-1">
                <label>{label ?? "passwordInputLabel"}</label>
            </div>
            <div>
                <input
                    type="password"
                    name={name ?? "password"}
                    placeholder={placeholder ?? ""}
                    onChange={handler}
                    className={_className ?? "h-10 w-full border-1 border rounded"}>
                </input>
            </div>
        </div>
    )
}

const PrimaryButton = ({_className, text, type, handler}) =>{
    return (
        <div>
             <button  
             type={type ?? "button"} 
             className={_className ?? "h-10 w-full border-0 border rounded text-white bg-blue-600" }>
             {text ?? "Button"}
             </button>
        </div>
    )
}
export {
    TextInput,
    PasswordInput,
    PrimaryButton
}
