import React from 'react'
import axios from 'axios'
import ChatInput from '../components/ChatInput'
import ProductCard from '../components/ProductCard'

export default function RecommendPage(){
  const [items, setItems] = React.useState([])
  const [blurbs, setBlurbs] = React.useState([])
  const [loading, setLoading] = React.useState(false)
  const [messages, setMessages] = React.useState([{role:'system', content:'You are a furniture assistant.'}])

  const send = async (text) => {
    const m = [...messages, {role:'user', content: text}]
    setMessages(m)
    setLoading(true)
    try{
      const res = await axios.post('http://localhost:8000/recommend/chat', { messages: m, top_k: 6 })
      setItems(res.data.products)
      setBlurbs(res.data.generated_descriptions)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <ChatInput onSend={send} />
      {loading && <div style={{marginTop:12}}>Thinking...</div>}
      <div style={{display:'grid', gridTemplateColumns:'1fr', gap:12, marginTop:12}}>
        {items.map((it, idx)=> <ProductCard key={it.uniq_id} item={it} blurb={blurbs[idx]} />)}
      </div>
    </div>
  )
}