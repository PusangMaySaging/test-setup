import React from 'react'
import {useQuery} from 'react-query'
const Home = () => {

    const {error, data, isLoading} = useQuery('sample', async()=>{
        const response = await fetch('http://localhost:1000/api/v1/products')
        return response.data
    })

    const lisItem = isLoading ? [] :data.map((d)=><span>{d.name}</span>)
    return (
        <div>           
             <h1>this is Home Page</h1>
             {listItem}
        </div>
    )
}

export default Home
