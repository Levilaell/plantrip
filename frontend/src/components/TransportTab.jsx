import React from 'react'

export default function TransportTab({ transports }) {
    return (
        <section>
            <h2>Transporte</h2>
            {transports.length === 0 ? (
                <p>Sem opções de transporte</p>
            ) : (
                <ul>
                    {transports.map((t, i) => (
                        <li key={i}>
                            {t.mode} {t.origin} → {t.destination} ({t.duration}) – R${t.price}
                        </li>
                    ))}
                </ul>
            )}
        </section>
    )
}
