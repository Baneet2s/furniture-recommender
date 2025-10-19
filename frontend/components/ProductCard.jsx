import React from 'react'

export default function ProductCard({ item, blurb }){
  const images = (() => {
    try { return JSON.parse(item.images) } catch { return [] }
  })()
  const img = images && images.length ? images[0] : null
  return (
    <div style={{border:'1px solid #ddd', borderRadius:12, padding:12, display:'flex', gap:12}}>
      {img ? <img src={img} alt={item.title} style={{width:120, height:120, objectFit:'cover', borderRadius:8}}/> : <div style={{width:120,height:120,background:'#f2f2f2',borderRadius:8}}/>}
      <div>
        <div style={{fontWeight:600}}>{item.title}</div>
        <div style={{opacity:.7, fontSize:14}}>{item.brand}</div>
        <div style={{marginTop:6}}>{blurb}</div>
        <div style={{marginTop:6, fontSize:14}}>Price: {item.price}</div>
        <div style={{fontSize:12, opacity:.7}}>Material: {item.material} • Color: {item.color}</div>
      </div>
    </div>
  )
}