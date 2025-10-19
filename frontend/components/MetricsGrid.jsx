import React from 'react'

export default function MetricsGrid({ stats }){
  const card = (label, value) => (
    <div style={{border:'1px solid #eee', padding:16, borderRadius:12}}>
      <div style={{opacity:.7, fontSize:14}}>{label}</div>
      <div style={{fontWeight:700, fontSize:22}}>{value}</div>
    </div>
  )
  return (
    <div style={{display:'grid', gridTemplateColumns:'repeat(4, 1fr)', gap:12}}>
      {card('Items', stats.n_items ?? '-')}
      {card('Avg Price', stats.avg_price ? `$${stats.avg_price.toFixed(2)}` : '-')}
      {card('Top Materials', stats.materials_top10 ? Object.keys(stats.materials_top10).slice(0,3).join(', ') : '-')}
      {card('Top Colors', stats.colors_top10 ? Object.keys(stats.colors_top10).slice(0,3).join(', ') : '-')}
    </div>
  )
}