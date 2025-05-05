import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import ItineraryList from './pages/ItineraryList'
import CreateItinerary from './pages/CreateItinerary'
import ItineraryDetail from './pages/ItineraryDetail'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/itineraries" replace />} />
        <Route path="/itineraries" element={<ItineraryList />} />
        <Route path="/itineraries/new" element={<CreateItinerary />} />
        <Route path="/itineraries/:id" element={<ItineraryDetail />} />
      </Routes>
    </BrowserRouter>
  )
}
