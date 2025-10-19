import React from 'react'

export default function ChatInput({ onSend }){
  const [text, setText] = React.useState('')
  return (
    <div style={{display:'flex', gap:8}}>
      <input value={text} onChange={e=>setText(e.target.value)} placeholder="Describe what you want... e.g., modern wooden dining chairs under $150" style={{flex:1, padding:10}}/>
      <button onClick={()=>{ if(text.trim()) { onSend(text); setText('') }}} style={{padding:'10px 14px'}}>Send</button>
    </div>
  )
}