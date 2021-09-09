import React from 'react'
import {useQuery} from 'react-query'
    
const fetchProducts = async()=>{
    const response = await fetch('http://localhost:1000/api/v1/products')
    return response.json()
}

const Home = () => {

    const {error, data:products, isLoading} = useQuery('sample', fetchProducts)   
    return !isLoading && !error ? (
        <div>           
             {
                 products.payload.map(d =>{
                    return <span key={d._id}>{d.name}</span>
                 })
             }
        </div>
    ):<span>LOADING....</span> 
    
}


export default Home
