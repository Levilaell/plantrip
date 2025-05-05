import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../services/api'

export default function CreateItinerary() {
    const [form, setForm] = useState({ destination: '', start_date: '', end_date: '', budget: '' })
    const nav = useNavigate()

    const handleChange = e =>
        setForm({ ...form, [e.target.name]: e.target.value })

    const handleSubmit = async e => {
        e.preventDefault()
        const res = await api.post('/itineraries/', form)
        nav(`/itineraries/${res.data.id}`)
    }

    return (
        <form onSubmit={handleSubmit}>
            <h1>Criar Itinerário</h1>
            <input name="destination" placeholder="Destino"
                value={form.destination} onChange={handleChange} required />
            <input name="start_date" type="date"
                value={form.start_date} onChange={handleChange} required />
            <input name="end_date" type="date"
                value={form.end_date} onChange={handleChange} required />
            <input name="budget" type="number" step="0.01"
                value={form.budget} onChange={handleChange} required />
            <button type="submit">Criar</button>
        </form>
    )
}
