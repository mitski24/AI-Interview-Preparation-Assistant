import { BrowserRouter, Routes, Route } from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import ChatPage from './pages/ChatPage'
import MockInterviewPage from './pages/MockInterviewPage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<LandingPage />} />
        <Route path='/chat' element={<ChatPage />} />
        <Route path='/mock' element={<MockInterviewPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App