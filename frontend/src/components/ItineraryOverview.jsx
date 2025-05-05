import React from 'react'

export default function ItineraryOverview({ destination, start_date, end_date, budget, generated }) {
    return (
        <header>
            <h1>{destination}</h1>
            <p>{start_date} → {end_date} • Orçamento: {budget}</p>
            {generated && <p>✅ Itinerário gerado</p>}
        </header>
    )
}