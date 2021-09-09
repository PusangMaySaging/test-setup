import { TextInput,PasswordInput,PrimaryButton} from "../components/Forms"
import { useState} from "react"
import axios from 'axios'



const Login = () => {

    const [formData,setFormData] = useState({})

    const formHandler = (element)=>{
        const {name, value} = element.target
        setFormData(prevState=>({
            ...prevState, [name]:value
        }))
    }
    const login = async(form) =>{
        form.preventDefault()
        try{
            const URL = 'http://localhost:1000/api/v1/login'
            const response = await axios.post(URL, formData)
            if(!response.data.success){
                throw(response.data.message)
            }
        }
        catch(error){
            console.log(error)
        }
   
    }

    return (
        <div className="grid grid-cols-12 grid-rows-4 h-screen">
            <div className="col-start-2 col-span-10 row-start-2 row-span-3 md:col-start-4 md:col-span-6 
                lg:col-start-5 lg:col-span-4">
                <div className="rounded-xl bg-white">
                <div className="p5 flex justify-center items-end h-12">
                    <span className="text-xl">Sign In</span>
                </div>
                <form className="flex flex-col h-72 justify-between p-8" onSubmit={login}>
                    <TextInput name="email" label="Email" handler={formHandler}/>
                    <PasswordInput label="Password" handler={formHandler}/>
                    <PrimaryButton type="submit" text="Sign In" />
                </form>
                </div>
            </div>
        </div>
    )
}

export default Login
