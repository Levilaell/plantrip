import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function ItineraryList() {
    const [list, setList] = useState([])

    useEffect(() => {
        api.getItineraries()
            .then(data => setList(data))
            .catch(err => console.error(err))
    }, [])


    return (
        <div>
            <h1>Meus Itinerários</h1>
            <Link to="/itineraries/new">+ Criar novo</Link>
            <ul>
                {list.map(i => (
                    <li key={i.id}>
                        <Link to={`/itineraries/${i.id}`}>
                            {i.destination} ({i.start_date} → {i.end_date})
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    )
}
