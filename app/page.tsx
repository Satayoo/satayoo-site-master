export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-purple-600 via-blue-600 to-cyan-500">
      <div className="container mx-auto px-4 py-16">
        <div className="flex flex-col items-center justify-center min-h-[80vh] text-white">
          <h1 className="text-6xl md:text-8xl font-bold mb-6 animate-fade-in">
            Satayoo
          </h1>
          <p className="text-xl md:text-2xl mb-8 text-center max-w-2xl opacity-90">
            Welcome to Satayoo - Your modern web experience starts here
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12 w-full max-w-4xl">
            <div className="bg-white/10 backdrop-blur-sm rounded-xl p-6 hover:bg-white/20 transition-colors">
              <h2 className="text-2xl font-semibold mb-3">✨ Modern Design</h2>
              <p className="opacity-80">Beautiful, responsive, and user-friendly interface built with the latest technologies.</p>
            </div>
            
            <div className="bg-white/10 backdrop-blur-sm rounded-xl p-6 hover:bg-white/20 transition-colors">
              <h2 className="text-2xl font-semibold mb-3">⚡ Lightning Fast</h2>
              <p className="opacity-80">Optimized performance with Next.js and deployed on Vercel&apos;s edge network.</p>
            </div>
            
            <div className="bg-white/10 backdrop-blur-sm rounded-xl p-6 hover:bg-white/20 transition-colors">
              <h2 className="text-2xl font-semibold mb-3">🚀 Ready to Scale</h2>
              <p className="opacity-80">Built with scalability in mind, ready to grow with your needs.</p>
            </div>
          </div>
          
          <div className="mt-12 flex gap-4">
            <button className="px-8 py-3 bg-white text-purple-600 rounded-full font-semibold hover:bg-gray-100 transition-colors">
              Get Started
            </button>
            <button className="px-8 py-3 border-2 border-white rounded-full font-semibold hover:bg-white/10 transition-colors">
              Learn More
            </button>
          </div>
        </div>
      </div>
    </main>
  )
}
