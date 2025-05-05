import React from 'react'

export default function ItineraryDay({ day }) {
    return (
        <div className="itinerary-day">
            <h3>{day.date}</h3>
            {day.summary && <p>{day.summary}</p>}
            <ul>
                {Object.entries(day.slots).map(([slotName, slotValue]) => (
                    <li key={slotName}>
                        <strong>{slotName.charAt(0).toUpperCase() + slotName.slice(1)}:</strong>{' '}
                        {typeof slotValue === 'object'
                            ? slotValue.summary + ` (${slotValue.temperature_c}°C)`
                            : slotValue}
                    </li>
                ))}
            </ul>
        </div>
    )
}
