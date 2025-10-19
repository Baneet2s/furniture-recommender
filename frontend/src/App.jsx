import React from 'react'
import { Link, useLocation } from 'react-router-dom'

export default function App({ children }){
  const loc = useLocation()
  return (
    <div style={{fontFamily:'Inter, system-ui', maxWidth: 1100, margin:'0 auto', padding: 16}}>
      <header style={{display:'flex', gap:16, alignItems:'center', justifyContent:'space-between'}}>
        <h2>🪑 Furniture Recommender</h2>
        <nav style={{display:'flex', gap:12}}>
          <Link to="/" style={{fontWeight: loc.pathname==='/'?'700':'400'}}>Recommend</Link>
          <Link to="/analytics" style={{fontWeight: loc.pathname==='/analytics'?'700':'400'}}>Analytics</Link>
        </nav>
      </header>
      <main style={{marginTop: 20}}>{children}</main>
    </div>
  )
}
