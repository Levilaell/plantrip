// src/services/api.js
import axios from 'axios'

const api = axios.create({
    baseURL: 'http://localhost/api',
    auth: {
        username: 'levilael',
        password: 'QWERasdf12'
    }
})

// dê um nome ao objeto
const apiService = {
    getItineraries: () => api.get('/itineraries/').then(r => r.data),
    getItinerary: id => api.get(`/itineraries/${id}/`).then(r => r.data),
    createItinerary: data => api.post('/itineraries/', data).then(r => r.data),
    // …outras chamadas
}

export default apiService
