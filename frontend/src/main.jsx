import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import App from './App'
import RecommendPage from './pages/RecommendPage'
import AnalyticsPage from './pages/AnalyticsPage'

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App>
      <Routes>
        <Route path="/" element={<RecommendPage />} />
        <Route path="/analytics" element={<AnalyticsPage />} />
      </Routes>
    </App>
  </BrowserRouter>
)