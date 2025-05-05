import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'
import ItineraryOverview from '../components/ItineraryOverview'
import ItineraryDay from '../components/ItineraryDay'
import TransportTab from '../components/TransportTab'
import AccommodationTab from '../components/AccommodationTab'

export default function ItineraryDetail() {
    const { id } = useParams()
    const [data, setData] = useState(null)

    useEffect(() => {
        api.getItinerary(id)
            .then(d => setData(d))
            .catch(err => console.error(err))
    }, [id])


    if (!data) return <p>Carregando…</p>

    return (
        <div>
            <ItineraryOverview  {...data} />
            <TransportTab transports={data.transports} />
            <AccommodationTab hotels={data.hotels} />
            {data.days.map(day => (
                <ItineraryDay key={day.date} {...day} />
            ))}
        </div>
    )
}
