import React from 'react'

export default function AccommodationTab({ hotels }) {
    return (
        <section>
            <h2>Hospedagem</h2>
            {hotels.length === 0 ? (
                <p>Sem opções de hospedagem</p>
            ) : (
                <ul>
                    {hotels.map((h, i) => (
                        <li key={i}>
                            {h.name} em {h.location} – R${h.price_per_night}/noite ({h.rating}★)
                        </li>
                    ))}
                </ul>
            )}
        </section>
    )
}
