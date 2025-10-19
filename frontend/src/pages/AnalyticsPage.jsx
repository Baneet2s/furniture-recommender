import React from 'react'
import axios from 'axios'
import MetricsGrid from '../components/MetricsGrid'

export default function AnalyticsPage(){
  const [stats, setStats] = React.useState({})
  React.useEffect(()=>{
    axios.get('http://localhost:8000/analytics/overview').then(r=>setStats(r.data))
  },[])
  return (
    <div>
      <MetricsGrid stats={stats} />
    </div>
  )
}