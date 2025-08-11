<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 relative">
    <!-- Mobile Menu Button -->
    <button 
      @click="sidebarOpen = !sidebarOpen"
      class="md:hidden fixed top-2 right-4 z-50 bg-white/90 backdrop-blur-sm border border-gray-200 rounded-lg p-2 shadow-lg hover:scale-105 transition-all duration-200"
    >
      <svg class="w-4 h-4 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
      </svg>
    </button>

    <div class="flex">
      <!-- Sidebar -->
      <aside 
        :class="[
          'fixed md:static inset-y-0 left-0 z-40 w-80 transform transition-all duration-300 ease-in-out md:translate-x-0',
          sidebarOpen ? 'translate-x-0' : '-translate-x-full'
        ]"
        style="background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.85) 50%, rgba(248,250,252,0.8) 80%, rgba(248,250,252,0.6) 90%, rgba(248,250,252,0.3) 95%, transparent 100%); backdrop-filter: blur(12px);"
      >
        <div class="p-6">
          <!-- Logo -->
          <div class="mb-8">
            <div class="flex items-center gap-3 mb-2">
              <div class="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg">
                <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
              </div>
              <div>
                <h1 class="text-xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Signal AI</h1>
                <p class="text-xs text-gray-500">Market Intelligence</p>
              </div>
            </div>
            <div class="flex items-center gap-2 mt-3">
              <div class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
              <span class="text-xs text-gray-600 font-medium">Live Analysis Active</span>
            </div>
          </div>

          <!-- Asset Categories -->
          <div class="space-y-3 mb-8">
            <button 
              v-for="category in assetCategories" 
              :key="category.id"
              @click="() => { activeCategory = category.id; sidebarOpen = false }"
              :class="[
                'group w-full text-left p-4 rounded-2xl transition-all duration-300 flex items-center space-x-3 hover:scale-105 hover:shadow-lg',
                activeCategory === category.id 
                  ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/25' 
                  : 'bg-white/70 backdrop-blur-sm text-gray-700 hover:bg-white/90 border border-gray-200/50'
              ]"
            >
              <div :class="[
                'w-12 h-12 rounded-2xl flex items-center justify-center text-xl transition-all duration-300',
                activeCategory === category.id 
                  ? 'bg-white/20 backdrop-blur-sm' 
                  : 'bg-gradient-to-br from-gray-100 to-gray-200 group-hover:from-blue-100 group-hover:to-purple-100'
              ]">
                {{ category.icon }}
              </div>
              <div class="flex-1">
                <div class="font-semibold text-sm">{{ category.name }}</div>
                <div :class="[
                  'text-xs mt-1',
                  activeCategory === category.id ? 'text-white/80' : 'text-gray-500'
                ]">{{ category.count }} assets tracked</div>
              </div>
              <div :class="[
                'w-2 h-8 rounded-full transition-all duration-300',
                activeCategory === category.id ? 'bg-white/30' : 'bg-transparent group-hover:bg-blue-200'
              ]"></div>
            </button>
          </div>

          <!-- Market Summary -->
          <div class="bg-gradient-to-br from-emerald-50 to-teal-100 rounded-2xl p-5 border border-emerald-200/50 mb-6 shadow-sm">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-8 h-8 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-xl flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                </svg>
              </div>
              <h3 class="text-sm font-bold text-emerald-800">Market Pulse</h3>
            </div>
            <p class="text-xs text-emerald-700 leading-relaxed">{{ marketSummary }}</p>
          </div>

          <!-- Top Story -->
          <div class="bg-gradient-to-br from-orange-50 to-red-100 rounded-2xl p-5 border border-orange-200/50 shadow-sm">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-8 h-8 bg-gradient-to-br from-orange-500 to-red-600 rounded-xl flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                </svg>
              </div>
              <h3 class="text-sm font-bold text-orange-800">Breaking News</h3>
            </div>
            <p class="text-xs text-orange-700 leading-relaxed">{{ topStory }}</p>
          </div>

          <!-- Email Subscription -->
          <div class="bg-gradient-to-br from-purple-50 to-indigo-100 rounded-2xl p-5 border border-purple-200/50 shadow-sm mt-6">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-8 h-8 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-xl flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17h-2v-2h2v2zm2.07-7.75l-.9.92C11.45 12.9 11 13.5 11 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H5.5c0-2.49 2.01-4.5 4.5-4.5s4.5 2.01 4.5 4.5c0 .88-.36 1.68-.93 2.25z"/>
                </svg>
              </div>
              <h3 class="text-sm font-bold text-purple-800">Daily Reports</h3>
            </div>
            <p class="text-xs text-purple-700 leading-relaxed mb-4">Get daily PDF reports delivered to your inbox</p>
            
            <form @submit.prevent="subscribeEmail" class="space-y-3">
              <div>
                <input 
                  v-model="subscriptionEmail"
                  type="email" 
                  placeholder="Enter your email"
                  required
                  class="w-full px-3 py-2 text-xs bg-white/70 backdrop-blur-sm border border-purple-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                >
              </div>
              <button 
                type="submit"
                :disabled="!subscriptionEmail || isSubscribing"
                class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 text-white text-xs font-medium py-2 px-4 rounded-lg hover:scale-105 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
              >
                <span v-if="isSubscribing">Subscribing...</span>
                <span v-else>Subscribe for Daily PDFs</span>
              </button>
            </form>
            
            <div v-if="subscriptionMessage" class="mt-3 p-2 rounded-lg text-xs" :class="subscriptionSuccess ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
              {{ subscriptionMessage }}
            </div>
          </div>
        </div>
      </aside>

      <!-- Overlay for mobile -->
      <div 
        v-if="sidebarOpen"
        @click="sidebarOpen = false"
        class="md:hidden fixed inset-0 bg-black bg-opacity-50 z-30"
      ></div>

      <!-- Main Content -->
      <main class="flex-1 md:ml-0 relative">
        <!-- Header -->
        <header class="bg-gradient-to-r from-white/70 via-white/75 to-slate-50/70 backdrop-blur-2xl px-2 py-1 md:px-4 md:py-2 sticky top-0 z-30">
          <div class="max-w-6xl mx-auto flex justify-between items-center">
            <div class="flex items-center gap-3">
              <!-- Mobile Brand Logo -->
              <div class="md:hidden flex items-center gap-1">
                <div class="w-4 h-4 bg-gradient-to-br from-blue-600 to-purple-600 rounded flex items-center justify-center">
                  <svg class="w-2 h-2 text-white" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M13 10V3L4 14h7v7l9-11h-7z"/>
                  </svg>
                </div>
                <span class="text-xs font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Signal AI</span>
              </div>
              
              <!-- Desktop Content -->
              <div class="hidden md:block">
                <h2 class="text-lg font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
                  {{ getCategoryName(activeCategory) }}
                </h2>
                <p class="text-xs text-gray-600 flex items-center gap-1">
                  <svg class="w-3 h-3 text-blue-500" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                  AI explains WHY assets move
                </p>
              </div>
              
              <!-- Mobile Category Title -->
              <div class="md:hidden">
                <h2 class="text-sm font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
                  {{ getCategoryName(activeCategory) }}
                </h2>
              </div>
            </div>
            <div class="text-right mr-12 md:mr-0 flex items-center gap-3">
              <!-- Pricing Button -->
              <button 
                class="hidden md:inline-flex items-center gap-1 px-3 py-1.5 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg text-xs font-medium hover:from-blue-700 hover:to-purple-700 transition-all shadow-sm"
                @click="showPricing = true"
              >
                💎 Premium $19/mo
              </button>
              
              <!-- Mobile Pricing -->
              <button 
                class="md:hidden px-2 py-1 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded text-xs font-medium"
                @click="showPricing = true"
              >
                💎
              </button>
              
              <div class="flex items-center gap-1 text-xs text-gray-500">
                <div class="w-1.5 h-1.5 md:w-2 md:h-2 bg-green-400 rounded-full animate-pulse"></div>
                <span class="font-medium text-xs">Live</span>
                <span class="font-mono text-green-600 text-xs">{{ currentTime }}</span>
              </div>
            </div>
          </div>
        </header>

        <!-- Content Area -->
        <div class="p-1 md:p-4">
          <div class="max-w-6xl mx-auto">
            
            <!-- Time Navigation & Reports Preview -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
              
              <!-- Time Travel Section -->
              <div v-if="historicalData.length > 0" class="bg-white/80 backdrop-blur-sm rounded-lg shadow-sm p-3">
                <div class="flex items-center justify-between mb-3">
                  <h3 class="font-semibold text-gray-800 flex items-center gap-2">
                    <span class="text-lg">⏰</span>
                    Time Travel
                  </h3>
                  <button 
                    v-if="isViewingHistorical"
                    @click="backToToday"
                    class="bg-gray-900 text-white px-3 py-1 rounded-lg hover:bg-gray-800 transition-colors text-sm font-medium"
                  >
                    Back to Live
                  </button>
                </div>
              <div class="flex gap-2 overflow-x-auto pb-1">
                <button 
                  @click="backToToday"
                  :class="[
                    'px-3 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all',
                    !isViewingHistorical 
                      ? 'bg-gray-900 text-white' 
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  ]"
                >
                  Live
                </button>
                <button 
                  v-for="day in historicalData" 
                  :key="day.date"
                  @click="viewHistoricalDay(day)"
                  :class="[
                    'px-3 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all flex flex-col items-center gap-1 min-w-[80px]',
                    selectedHistoricalDay?.date === day.date 
                      ? 'bg-blue-600 text-white' 
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  ]"
                >
                  <span>{{ day.displayDate || formatDate(day.date) }}</span>
                  <div class="flex items-center gap-1 text-xs">
                    <span :class="getDirectionColor(day.market_direction)">
                      {{ day.market_direction === 'Bullish' ? '↗' : day.market_direction === 'Bearish' ? '↘' : '→' }}
                    </span>
                    <span class="opacity-75">{{ day.confidence || 0 }}%</span>
                  </div>
                </button>
              </div>
              </div>
              
              <!-- Reports Preview Section -->
              <div v-if="currentReports && currentReports.length > 0" class="bg-white/80 backdrop-blur-sm rounded-lg shadow-sm p-3">
                <div class="flex items-center justify-between mb-3">
                  <h3 class="font-semibold text-gray-800 flex items-center gap-2">
                    <span class="text-lg">📄</span>
                    Today's Reports
                  </h3>
                  <button 
                    class="text-blue-600 hover:text-blue-700 text-xs font-medium"
                    @click="showReportsSidebar = true"
                  >
                    View All →
                  </button>
                </div>
                <div class="flex gap-2 overflow-x-auto pb-1">
                  <button 
                    v-for="report in currentReports.slice(0, 4)" 
                    :key="report.id"
                    @click="previewReport(report)"
                    class="flex-shrink-0 bg-gradient-to-r from-blue-50 to-purple-50 hover:from-blue-100 hover:to-purple-100 border border-blue-200 rounded-lg p-2 transition-all text-left min-w-[120px]"
                  >
                    <div class="text-xs font-medium text-gray-800 mb-1">{{ report.title }}</div>
                    <div class="text-xs text-gray-600 mb-1">{{ report.date }}</div>
                    <div class="flex items-center justify-between">
                      <span class="text-xs px-2 py-0.5 bg-blue-100 text-blue-700 rounded-full">
                        {{ report.market_direction }}
                      </span>
                      <span class="text-xs text-gray-500">{{ report.confidence }}%</span>
                    </div>
                  </button>
                </div>
              </div>
              
            </div>

            <!-- Historical Warning -->
            <div v-if="isViewingHistorical" class="bg-amber-50/80 backdrop-blur-sm rounded-xl shadow-sm p-2 md:p-3 mb-2 md:mb-4">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-amber-100 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-amber-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                </div>
                <div>
                  <p class="font-semibold text-amber-800">Viewing {{ formatDate(selectedHistoricalDay.date) }} Data</p>
                  <p class="text-sm text-amber-700">Historical analysis - click "Back to Live" for current market data</p>
                </div>
              </div>
            </div>

            <!-- Market Overview -->
            <div class="bg-white/80 backdrop-blur-sm rounded-lg shadow-sm p-1 md:p-4 mb-1 md:mb-4">
              <div class="flex items-center justify-between mb-1 md:mb-3">
                <h2 class="text-sm md:text-lg font-bold text-gray-900">Overview</h2>
                <div class="flex items-center gap-1">
                  <div class="w-1.5 h-1.5 md:w-2 md:h-2 bg-green-500 rounded-full animate-pulse"></div>
                  <span class="text-xs text-gray-600 hidden md:block">Live AI Analysis</span>
                </div>
              </div>
              
              <!-- Today's Stats -->
              <div class="grid grid-cols-5 gap-1 md:gap-3 mb-1 md:mb-4">
                <div class="text-center p-1 md:p-2 bg-gray-50/70 backdrop-blur-sm rounded-lg">
                  <div :class="getDirectionColor(marketPrediction.direction)" class="text-sm md:text-lg font-bold mb-0.5">
                    {{ marketPrediction.direction }}
                  </div>
                  <div class="text-xs text-gray-500">Trend</div>
                </div>
                <div class="text-center p-1 md:p-2 bg-gray-50/70 backdrop-blur-sm rounded-lg">
                  <div class="text-sm md:text-lg font-bold text-gray-900 mb-0.5">{{ filteredAssets.length }}</div>
                  <div class="text-xs text-gray-500">Assets</div>
                </div>
                <div class="text-center p-1 md:p-2 bg-green-50/70 backdrop-blur-sm rounded-lg">
                  <div class="text-sm md:text-lg font-bold text-green-600 mb-0.5">{{ getPositiveCount() }}</div>
                  <div class="text-xs text-gray-500">Up</div>
                </div>
                <div class="text-center p-1 md:p-2 bg-red-50/70 backdrop-blur-sm rounded-lg">
                  <div class="text-sm md:text-lg font-bold text-red-600 mb-0.5">{{ getNegativeCount() }}</div>
                  <div class="text-xs text-gray-500">Down</div>
                </div>
                <div class="text-center p-1 md:p-2 bg-blue-50/70 backdrop-blur-sm rounded-lg">
                  <div class="text-sm md:text-lg font-bold text-blue-600 mb-0.5">{{ marketPrediction.confidence }}%</div>
                  <div class="text-xs text-gray-500">AI Confidence</div>
                </div>
              </div>

              <!-- AI Trading Insights - Hidden on mobile -->
              <div class="hidden md:block mt-3 pt-3 border-t border-gray-100/50">
                <h3 class="text-sm font-semibold text-gray-900 mb-2 flex items-center gap-2">
                  🎯 Quick Insights
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
                  <div class="bg-blue-50/60 backdrop-blur-sm rounded-xl p-2">
                    <div class="flex items-center gap-1 mb-1">
                      <div class="w-2 h-2 bg-blue-500 rounded-full"></div>
                      <h4 class="font-medium text-gray-900 text-xs">Today</h4>
                    </div>
                    <p class="text-xs text-gray-700 mb-1 line-clamp-2">{{ getTodaysTrend() }}</p>
                    <div class="text-xs text-blue-600 font-medium">
                      Top: {{ getTopMovers().slice(0,2).join(', ') }}
                    </div>
                  </div>
                  <div class="bg-purple-50/60 backdrop-blur-sm rounded-xl p-2">
                    <div class="flex items-center gap-1 mb-1">
                      <div class="w-2 h-2 bg-purple-500 rounded-full"></div>
                      <h4 class="font-medium text-gray-900 text-xs">Weekly</h4>
                    </div>
                    <p class="text-xs text-gray-700 mb-1 line-clamp-2">{{ getWeeklyPrediction() }}</p>
                    <div class="text-xs text-purple-600 font-medium">
                      Target: {{ marketPrediction.target }}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Asset Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              <div 
                v-for="asset in filteredAssets" 
                :key="asset.symbol"
                class="group bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-gray-200/50 p-4 hover:shadow-xl hover:scale-[1.02] transition-all duration-300 cursor-pointer hover:bg-white/95 relative overflow-hidden"
                @click="viewAssetDetails(asset)"
              >
                <!-- Subtle gradient background -->
                <div class="absolute inset-0 bg-gradient-to-br from-blue-50/50 via-transparent to-purple-50/50 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                
                  <!-- Asset Header -->
                  <div class="flex justify-between items-start mb-3">
                    <div class="flex items-center gap-3">
                      <div :class="getIconStyle(asset.asset_type)" class="w-10 h-10 rounded-xl flex items-center justify-center shadow-sm group-hover:scale-110 transition-transform duration-300">
                        <span class="text-lg">{{ getAssetIcon(asset.asset_type) }}</span>
                      </div>
                      <div>
                        <h3 class="font-bold text-gray-900 text-lg mb-0.5">{{ asset.symbol.split(' ')[0] }}</h3>
                        <p class="text-xs text-gray-600 font-medium">{{ getAssetDescription(asset).split(' - ')[1] || getAssetDescription(asset) }}</p>
                      </div>
                    </div>
                    <div class="text-right">
                      <div 
                        class="text-lg font-bold mb-1"
                        :class="getMoveColor(asset.current_move)"
                      >
                        {{ asset.current_move }}
                      </div>
                      <span 
                        class="px-2 py-1 rounded-lg text-xs font-bold"
                        :class="getActionStyle(asset.action)"
                      >
                        {{ asset.action.toUpperCase() }}
                      </span>
                    </div>
                  </div>

                  <!-- AI Insight -->
                  <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-3 mb-3 border border-blue-100/50">
                    <div class="flex items-center gap-2 mb-2">
                      <div class="w-6 h-6 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                        <svg class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 24 24">
                          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                        </svg>
                      </div>
                      <h4 class="text-xs font-bold text-blue-800">AI Analysis</h4>
                    </div>
                    <p class="text-xs text-blue-900 leading-relaxed font-medium line-clamp-2 mb-3">{{ asset.why_simple }}</p>
                    
                    <!-- Target and Risk in AI Analysis box -->
                    <div class="grid grid-cols-2 gap-3 mt-2 pt-2 border-t border-blue-200/50">
                      <div class="text-center">
                        <div class="text-xs text-blue-700 font-medium mb-1">Target</div>
                        <div class="text-sm font-bold text-green-700">
                          {{ extractPrice(asset.profit_target || asset.next_target) || asset.next_target || 'TBD' }}
                        </div>
                      </div>
                      <div class="text-center">
                        <div class="text-xs text-blue-700 font-medium mb-1">Risk</div>
                        <div :class="getRiskStyle(asset.risk)" class="text-xs px-2 py-1 rounded-full font-bold inline-block">
                          {{ asset.risk?.toUpperCase() || 'MEDIUM' }}
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Entry Signal Box -->
                  <div class="bg-gradient-to-r from-green-50 via-blue-50 to-purple-50 rounded-lg p-3 mb-3 border border-green-200/50">
                    <div class="flex items-center justify-between mb-2">
                      <div class="flex items-center gap-1">
                        <span class="text-green-600">🎯</span>
                        <span class="text-xs font-bold text-gray-800">ENTRY SIGNAL</span>
                      </div>
                      <span class="text-xs px-2 py-1 bg-white rounded-full font-bold text-green-700">
                        {{ asset.action?.toUpperCase() }}
                      </span>
                    </div>
                  </div>

                  <!-- Click to expand indicator -->
                  <div class="flex items-center justify-center pt-2 border-t border-gray-100/50">
                    <div class="flex items-center gap-1 text-xs text-gray-500 group-hover:text-blue-600 transition-colors duration-200">
                      <span class="font-medium">Tap for details</span>
                      <svg class="w-3 h-3 group-hover:translate-x-0.5 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                      </svg>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Loading State -->
            <div v-if="loading" class="text-center py-12">
              <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900 mx-auto mb-4"></div>
              <p class="text-gray-600">AI is analyzing {{ getCategoryName(activeCategory).toLowerCase() }}...</p>
            </div>

            <!-- No Data State -->
            <div v-if="!loading && filteredAssets.length === 0" class="text-center py-12">
              <p class="text-gray-600 mb-4">No {{ getCategoryName(activeCategory).toLowerCase() }} analysis available</p>
              <button 
                @click="loadData" 
                class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
              >
                Refresh Analysis
              </button>
            </div>
          </div>
          
          
            </main>
        </div>
        
        <!-- Reports Sidebar -->
        <div v-if="showReportsSidebar" class="fixed inset-0 z-50 overflow-hidden">
          <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" @click="showReportsSidebar = false"></div>
          <div class="absolute right-0 top-0 h-full w-full max-w-md bg-white shadow-xl">
            <div class="flex flex-col h-full">
              <!-- Header -->
              <div class="p-4 border-b border-gray-200">
                <div class="flex items-center justify-between">
                  <h2 class="text-xl font-bold text-gray-900 flex items-center gap-2">
                    <span class="text-lg">📄</span>
                    Premium Reports
                  </h2>
                  <button 
                    @click="showReportsSidebar = false"
                    class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
                <p class="text-sm text-gray-600 mt-1">Current reports by date</p>
              </div>
              
              <!-- Reports List -->
              <div class="flex-1 overflow-y-auto p-4 space-y-4">
                <div 
                  v-for="report in currentReports" 
                  :key="report.id"
                  class="bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-4 border border-blue-100"
                >
                  <div class="flex items-start justify-between mb-2">
                    <h3 class="font-medium text-gray-900">{{ report.title }}</h3>
                    <span class="text-xs px-2 py-1 bg-blue-100 text-blue-700 rounded-full">
                      {{ report.market_direction }}
                    </span>
                  </div>
                  <p class="text-sm text-gray-600 mb-3">{{ report.date }}</p>
                  <div class="space-y-1 mb-3">
                    <div v-for="highlight in report.key_highlights.slice(0, 2)" :key="highlight" 
                         class="text-xs text-gray-700 flex items-start gap-1">
                      <span class="text-blue-500 mt-0.5">•</span>
                      <span>{{ highlight }}</span>
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <button 
                      @click="previewReport(report)"
                      class="flex-1 px-3 py-2 bg-blue-100 text-blue-700 rounded text-sm font-medium hover:bg-blue-200 transition-colors"
                    >
                      Preview
                    </button>
                    <a 
                      :href="report.pdf_url" 
                      :download="'SignalAI_Sample_Report_' + report.id + '.pdf'"
                      class="flex-1 px-3 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded text-sm font-medium hover:from-blue-700 hover:to-purple-700 transition-all text-center"
                    >
                      Download
                    </a>
                  </div>
                </div>
              </div>
              
              <!-- CTA Footer -->
              <div class="p-4 border-t border-gray-200 bg-gradient-to-r from-blue-600 to-purple-600 text-white">
                <h3 class="font-bold mb-1">Get Daily Reports</h3>
                <p class="text-xs text-blue-100 mb-3">Professional analysis delivered every morning</p>
                <button 
                  @click="showPricing = true; showReportsSidebar = false"
                  class="w-full bg-white text-blue-600 px-4 py-2 rounded-lg font-medium hover:bg-blue-50 transition-colors"
                >
                  Start Free Trial - $19/mo
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Pricing Modal -->
        <div v-if="showPricing" class="fixed inset-0 z-50 overflow-y-auto">
          <div class="flex items-center justify-center min-h-screen px-4">
            <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" @click="showPricing = false"></div>
            <div class="relative bg-white rounded-2xl shadow-2xl max-w-lg w-full p-6">
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-2xl font-bold text-gray-900">💎 Premium Plans</h2>
                <button 
                  @click="showPricing = false"
                  class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
                >
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
              
              <!-- Single Premium Plan -->
              <div class="border-2 border-purple-300 rounded-xl p-6 bg-gradient-to-r from-purple-600 to-blue-600 text-white relative">
                <div class="absolute -top-3 left-4 bg-yellow-400 text-black px-3 py-1 rounded-full text-xs font-bold">
                  PREMIUM
                </div>
                <div class="flex justify-between items-center mb-3">
                  <h3 class="font-bold text-2xl">Daily Reports</h3>
                  <div class="text-right">
                    <span class="text-3xl font-bold">$19</span>
                    <div class="text-sm text-blue-100">per month</div>
                  </div>
                </div>
                <ul class="space-y-3 text-sm mb-6">
                  <li class="flex items-center gap-3">
                    <svg class="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                    <span>Daily PDF reports delivered to your inbox</span>
                  </li>
                  <li class="flex items-center gap-3">
                    <svg class="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                    <span>AI-powered global market analysis</span>
                  </li>
                  <li class="flex items-center gap-3">
                    <svg class="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                    <span>Email alerts for major market moves</span>
                  </li>
                  <li class="flex items-center gap-3">
                    <svg class="w-5 h-5 text-green-300" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                    <span>Professional trading insights & recommendations</span>
                  </li>
                </ul>
              </div>
              
              <div class="mt-6 pt-4 border-t border-gray-200">
                <!-- Email Subscription Form -->
                <div class="mb-4">
                  <label class="block text-sm font-medium text-gray-700 mb-2">
                    📧 Get Daily Reports via Email
                  </label>
                  <div class="flex gap-2">
                    <input 
                      v-model="subscriptionEmail"
                      type="email" 
                      placeholder="Enter your email"
                      class="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
                    />
                    <button 
                      @click="subscribeToReports"
                      :disabled="subscriptionLoading"
                      class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors disabled:bg-blue-400 text-sm font-medium whitespace-nowrap"
                    >
                      {{ subscriptionLoading ? '...' : 'Subscribe' }}
                    </button>
                  </div>
                  <div v-if="subscriptionMessage" class="mt-2 text-xs" :class="subscriptionSuccess ? 'text-green-600' : 'text-red-600'">
                    {{ subscriptionMessage }}
                  </div>
                </div>
                
                <p class="text-xs text-gray-500 text-center mb-4">
                  Free daily reports • Professional analysis • Cancel anytime
                </p>
                <button 
                  class="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-3 rounded-lg font-bold hover:from-blue-700 hover:to-purple-700 transition-all"
                  @click="showPricing = false"
                >
                  Continue to Dashboard
                </button>
              </div>
            </div>
          </div>
        </div>
        
    </div>

  

    <!-- Asset Details Modal -->
    <div v-if="showAssetDetails" class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div class="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <!-- Modal Header -->
        <div class="sticky top-0 bg-white border-b border-gray-200 px-6 py-4 rounded-t-2xl">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div :class="getIconStyle(selectedAsset?.asset_type)" class="w-12 h-12 rounded-full flex items-center justify-center">
                <span class="text-xl">{{ getAssetIcon(selectedAsset?.asset_type) }}</span>
              </div>
              <div>
                <h2 class="text-2xl font-bold text-gray-900">{{ selectedAsset?.symbol }}</h2>
                <p class="text-sm text-gray-500">{{ getAssetDescription(selectedAsset) }}</p>
              </div>
            </div>
            <button 
              @click="closeAssetDetails"
              class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Modal Content -->
        <div class="p-6">
          <!-- Quick Trade Setup (Always Visible at Top) -->
          <div v-if="selectedAsset && !loadingDetails" class="bg-gradient-to-r from-green-50 via-blue-50 to-purple-50 rounded-xl p-6 mb-6 border-2 border-green-200">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 bg-gradient-to-br from-green-500 to-blue-600 rounded-xl flex items-center justify-center">
                <span class="text-2xl">🎯</span>
              </div>
              <div>
                <h3 class="text-xl font-bold text-gray-900">TRADE SETUP</h3>
                <p class="text-sm text-gray-600">AI-Generated Entry Points</p>
              </div>
              <div class="ml-auto">
                <span :class="getActionStyle(selectedAsset.action)" class="px-4 py-2 rounded-xl text-sm font-bold">
                  {{ selectedAsset.action?.toUpperCase() }} SIGNAL
                </span>
              </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div class="bg-white rounded-lg p-4 border border-blue-200 text-center">
                <div class="text-xs text-gray-600 mb-1">ENTRY PRICE</div>
                <div class="text-lg font-bold text-blue-600">{{ detailedAnalysis?.trading_signals?.entry_price || selectedAsset?.entry_price || selectedAsset.current_move }}</div>
                <div class="text-xs text-gray-500 mt-1">Current: {{ selectedAsset.current_move }}</div>
              </div>
              <div class="bg-white rounded-lg p-4 border border-red-200 text-center">
                <div class="text-xs text-gray-600 mb-1">STOP LOSS</div>
                <div class="text-lg font-bold text-red-600">{{ detailedAnalysis?.trading_signals?.stop_loss || selectedAsset?.stop_loss || 'Set -5%' }}</div>
                <div class="text-xs text-gray-500 mt-1">Risk protection</div>
              </div>
              <div class="bg-white rounded-lg p-4 border border-green-200 text-center">
                <div class="text-xs text-gray-600 mb-1">TAKE PROFIT</div>
                <div class="text-lg font-bold text-green-600">{{ detailedAnalysis?.trading_signals?.take_profit || selectedAsset?.profit_target || selectedAsset.next_target }}</div>
                <div class="text-xs text-gray-500 mt-1">Profit target</div>
              </div>
              <div class="bg-white rounded-lg p-4 border border-purple-200 text-center">
                <div class="text-xs text-gray-600 mb-1">RISK:REWARD</div>
                <div class="text-lg font-bold text-purple-600">{{ detailedAnalysis?.trading_signals?.risk_reward_ratio || '1:2' }}</div>
                <div class="text-xs text-gray-500 mt-1">Profit ratio</div>
              </div>
            </div>
            
            <div class="mt-4 bg-yellow-50 border border-yellow-200 rounded-lg p-3">
              <div class="flex items-start gap-2">
                <span class="text-yellow-600 text-lg">💡</span>
                <div>
                  <h4 class="font-bold text-yellow-800 text-sm">Why This Trade:</h4>
                  <p class="text-yellow-700 text-sm mt-1">{{ selectedAsset?.trade_setup || selectedAsset.why_simple }}</p>
                  <div v-if="selectedAsset?.time_sensitive" class="mt-2 text-xs text-yellow-600 font-medium">
                    ⏰ Time Sensitive - Act quickly on this opportunity
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Loading State -->
          <div v-if="loadingDetails" class="text-center py-12">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto mb-4"></div>
            <p class="text-gray-600">Loading detailed analysis...</p>
          </div>
          
          <!-- Error State -->
          <div v-else-if="detailedAnalysis?.error" class="text-center py-8">
            <div class="text-gray-500 mb-2">⚠️</div>
            <p class="text-gray-600">Detailed analysis not available</p>
          </div>
          
          <!-- Detailed Analysis Content -->
          <div v-else-if="detailedAnalysis">
            <!-- Price & Performance Overview -->
            <div class="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6 mb-6">
              <h3 class="text-lg font-bold text-gray-900 mb-4">Price & Performance</h3>
              <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div class="text-2xl font-bold text-gray-900 mb-1">
                    {{ detailedAnalysis.current_price }}
                  </div>
                  <div class="text-sm text-gray-500">Current Price</div>
                </div>
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div :class="getMoveColor(detailedAnalysis.price_change_24h)" class="text-xl font-bold mb-1">
                    {{ detailedAnalysis.price_change_24h }}
                  </div>
                  <div class="text-sm text-gray-500">24h Change</div>
                </div>
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div :class="getMoveColor(detailedAnalysis.price_change_7d)" class="text-xl font-bold mb-1">
                    {{ detailedAnalysis.price_change_7d }}
                  </div>
                  <div class="text-sm text-gray-500">7d Change</div>
                </div>
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div class="text-xl font-bold text-gray-900 mb-1">
                    {{ detailedAnalysis.volume_24h }}
                  </div>
                  <div class="text-sm text-gray-500">Volume</div>
                </div>
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div class="text-xl font-bold text-gray-900 mb-1">
                    {{ detailedAnalysis.market_cap }}
                  </div>
                  <div class="text-sm text-gray-500">Market Cap</div>
                </div>
              </div>
            </div>

            <!-- Live Price Chart -->
            <div class="bg-white rounded-xl border border-gray-200 p-6 mb-6">
              <div class="flex items-center justify-between mb-4">
                <h4 class="text-lg font-semibold text-gray-900">Intraday Price Chart</h4>
                <div class="flex gap-2">
                  <button class="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded-lg font-medium">1D</button>
                  <button class="px-3 py-1 text-xs bg-gray-100 text-gray-600 rounded-lg">1W</button>
                  <button class="px-3 py-1 text-xs bg-gray-100 text-gray-600 rounded-lg">1M</button>
                </div>
              </div>
              
              <!-- Price Chart with Real Data -->
              <div class="bg-gray-50 rounded-lg p-4">
                <div class="flex items-end justify-between h-32 mb-4">
                  <div v-for="(point, index) in detailedAnalysis.price_history" :key="index" 
                       class="flex-1 flex flex-col items-center">
                    <div 
                      :style="{ height: Math.max(10, (point.price / Math.max(...detailedAnalysis.price_history.map(p => p.price))) * 100) + 'px' }"
                      class="w-8 bg-gradient-to-t from-blue-400 to-blue-600 rounded-t mb-1 mx-1"
                    ></div>
                    <div class="text-xs text-gray-500">{{ point.time }}</div>
                  </div>
                </div>
                <div class="grid grid-cols-3 gap-4 text-sm border-t pt-3">
                  <div>
                    <div class="text-gray-500">High</div>
                    <div class="font-medium">${{ Math.max(...detailedAnalysis.price_history.map(p => p.price)).toFixed(2) }}</div>
                  </div>
                  <div>
                    <div class="text-gray-500">Current</div>
                    <div class="font-medium">{{ detailedAnalysis.current_price }}</div>
                  </div>
                  <div>
                    <div class="text-gray-500">Low</div>
                    <div class="font-medium">${{ Math.min(...detailedAnalysis.price_history.map(p => p.price)).toFixed(2) }}</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Technical Indicators -->
            <div class="bg-white rounded-xl border border-gray-200 p-6 mb-6">
              <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <span>⚡</span> Technical Indicators
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div>
                  <h4 class="font-semibold text-gray-800 mb-3">Key Metrics</h4>
                  <div class="space-y-2">
                    <div class="flex justify-between">
                      <span class="text-gray-600">RSI:</span>
                      <span class="font-medium" :class="detailedAnalysis.technical_indicators.rsi > 70 ? 'text-red-600' : detailedAnalysis.technical_indicators.rsi < 30 ? 'text-green-600' : 'text-gray-900'">
                        {{ detailedAnalysis.technical_indicators.rsi }}
                      </span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-gray-600">MACD:</span>
                      <span class="font-medium capitalize" :class="detailedAnalysis.technical_indicators.macd === 'bullish' ? 'text-green-600' : detailedAnalysis.technical_indicators.macd === 'bearish' ? 'text-red-600' : 'text-gray-600'">
                        {{ detailedAnalysis.technical_indicators.macd }}
                      </span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-gray-600">Trend:</span>
                      <span class="font-medium capitalize" :class="detailedAnalysis.technical_indicators.trend === 'bullish' ? 'text-green-600' : detailedAnalysis.technical_indicators.trend === 'bearish' ? 'text-red-600' : 'text-gray-600'">
                        {{ detailedAnalysis.technical_indicators.trend }}
                      </span>
                    </div>
                  </div>
                </div>
                <div>
                  <h4 class="font-semibold text-gray-800 mb-3">Support Levels</h4>
                  <div class="space-y-1">
                    <div v-for="level in detailedAnalysis.technical_indicators.support_levels" :key="level" class="text-sm text-green-600 font-medium">
                      {{ level }}
                    </div>
                  </div>
                </div>
                <div>
                  <h4 class="font-semibold text-gray-800 mb-3">Resistance Levels</h4>
                  <div class="space-y-1">
                    <div v-for="level in detailedAnalysis.technical_indicators.resistance_levels" :key="level" class="text-sm text-red-600 font-medium">
                      {{ level }}
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Trading Signals -->
            <div class="bg-white rounded-xl border border-gray-200 p-6 mb-6">
              <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <span>🎯</span> Trading Signals
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-gradient-to-r from-green-50 to-blue-50 rounded-lg p-4">
                  <div class="flex items-center justify-between mb-3">
                    <span class="font-semibold text-gray-800">Primary Signal</span>
                    <span :class="getActionStyle(detailedAnalysis.trading_signals.primary_signal)" class="px-3 py-1 rounded-lg text-sm font-bold">
                      {{ detailedAnalysis.trading_signals.primary_signal }}
                    </span>
                  </div>
                  <div class="space-y-2 text-sm">
                    <div class="flex justify-between">
                      <span class="text-gray-600">Strength:</span>
                      <span class="font-medium text-blue-500">{{ detailedAnalysis.trading_signals.signal_strength }}</span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-gray-600">Time Horizon:</span>
                      <span class="font-medium text-blue-500">{{ detailedAnalysis.trading_signals.time_horizon }}</span>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 rounded-lg p-4">
                  <h4 class="font-semibold text-gray-800 mb-3">Trade Setup</h4>
                  <div class="space-y-2 text-sm">
                    <div class="flex justify-between">
                      <span class="text-gray-600">Entry:</span>
                      <span class="font-medium text-blue-500">{{ detailedAnalysis.trading_signals.entry_price }}</span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-gray-600">Stop Loss:</span>
                      <span class="font-medium text-red-600">{{ detailedAnalysis.trading_signals.stop_loss }}</span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-gray-600">Take Profit:</span>
                      <span class="font-medium text-green-600">{{ detailedAnalysis.trading_signals.take_profit }}</span>
                    </div>
                    <div class="flex justify-between">
                      <span class="text-gray-600">R:R Ratio:</span>
                      <span class="font-medium text-blue-500">{{ detailedAnalysis.trading_signals.risk_reward_ratio }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Market Sentiment -->
            <div class="bg-white rounded-xl border border-gray-200 p-6 mb-6">
              <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <span>📊</span> Market Sentiment & Analysis
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <div class="bg-blue-50 rounded-lg p-4 mb-4">
                    <div class="flex items-center justify-between mb-2">
                      <span class="font-semibold text-gray-800">Overall Sentiment</span>
                      <span :class="detailedAnalysis.news_sentiment.overall_sentiment === 'Positive' ? 'text-green-600' : detailedAnalysis.news_sentiment.overall_sentiment === 'Negative' ? 'text-red-600' : 'text-gray-600'" class="font-bold">
                        {{ detailedAnalysis.news_sentiment.overall_sentiment }}
                      </span>
                    </div>
                    <div class="w-full bg-gray-200 rounded-full h-2 mb-2">
                      <div class="bg-blue-600 h-2 rounded-full" :style="{ width: (detailedAnalysis.news_sentiment.sentiment_score * 100) + '%' }"></div>
                    </div>
                    <div class="text-sm text-gray-600">Score: {{ detailedAnalysis.news_sentiment.sentiment_score }}/1.0</div>
                  </div>
                  
                  <div class="space-y-2">
                    <h4 class="font-semibold text-gray-800">Key Factors:</h4>
                    <div v-for="factor in detailedAnalysis.news_sentiment.key_news_factors" :key="factor" class="text-sm text-gray-700 bg-gray-50 rounded px-2 py-1">
                      • {{ factor }}
                    </div>
                  </div>
                </div>
                
                <div>
                  <h4 class="font-semibold text-gray-800 mb-3">Professional Analysis</h4>
                  <p class="text-gray-700 text-sm leading-relaxed mb-4">{{ detailedAnalysis.detailed_explanation }}</p>
                  <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                    <h5 class="font-semibold text-yellow-800 mb-1">Trading Recommendation:</h5>
                    <p class="text-yellow-700 text-sm">{{ detailedAnalysis.trading_recommendation }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Fallback to basic data -->
          <div v-else>
            <!-- Basic Performance -->
            <div class="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6 mb-6">
              <h3 class="text-lg font-bold text-gray-900 mb-4">Current Performance</h3>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div :class="getMoveColor(selectedAsset?.current_move)" class="text-3xl font-bold mb-1">
                    {{ selectedAsset?.current_move }}
                  </div>
                  <div class="text-sm text-gray-500">Price Movement</div>
                </div>
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div :class="getActionStyle(selectedAsset?.action)" class="text-sm font-semibold px-3 py-1 rounded-lg inline-block mb-1">
                    {{ selectedAsset?.action?.toUpperCase() }}
                  </div>
                  <div class="text-sm text-gray-500 mt-2">AI Recommendation</div>
                </div>
                <div class="text-center p-4 bg-white rounded-lg shadow-sm">
                  <div :class="getRiskStyle(selectedAsset?.risk)" class="text-sm font-medium px-3 py-1 rounded-lg inline-block mb-1">
                    {{ selectedAsset?.risk?.toUpperCase() }}
                  </div>
                  <div class="text-sm text-gray-500 mt-2">Risk Level</div>
                </div>
              </div>
            </div>

          <!-- AI Analysis -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <!-- Why It's Moving -->
            <div class="bg-white rounded-xl border border-gray-200 p-6">
              <div class="flex items-center gap-2 mb-4">
                <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                  <span class="text-sm">🧠</span>
                </div>
                <h4 class="text-lg font-semibold text-gray-900">Why It's Moving</h4>
              </div>
              <p class="text-gray-700 leading-relaxed mb-4">{{ selectedAsset?.why_simple }}</p>
              <div class="text-sm text-blue-600 font-medium">
                Primary Catalyst: {{ selectedAsset?.catalyst || 'Market dynamics' }}
              </div>
            </div>

            <!-- Technical Analysis -->
            <div class="bg-white rounded-xl border border-gray-200 p-6">
              <div class="flex items-center gap-2 mb-4">
                <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                  <span class="text-sm">📈</span>
                </div>
                <h4 class="text-lg font-semibold text-gray-900">Technical Outlook</h4>
              </div>
              <p class="text-gray-700 leading-relaxed mb-4">{{ selectedAsset?.market_prediction }}</p>
              <div class="space-y-2">
                <div class="flex justify-between text-sm">
                  <span class="text-gray-500">Next Target:</span>
                  <span class="font-medium text-gray-900">{{ selectedAsset?.next_target }}</span>
                </div>
                <div class="flex justify-between text-sm">
                  <span class="text-gray-500">Confidence:</span>
                  <span class="font-medium text-gray-900">{{ selectedAsset?.confidence?.toUpperCase() }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Enhanced Analysis Section -->
          <div class="space-y-6 mb-6">
            <!-- Why It's Moving (Prominent) -->
            <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center">
                  <span class="text-white text-lg">🧠</span>
                </div>
                <h4 class="text-xl font-bold text-gray-900">Why {{ selectedAsset?.symbol }} is Moving</h4>
              </div>
              <div class="space-y-4">
                <div class="bg-white rounded-lg p-4 border border-blue-100">
                  <h5 class="font-semibold text-blue-800 mb-2">Simple Explanation:</h5>
                  <p class="text-gray-700 text-base leading-relaxed">{{ selectedAsset?.why_simple }}</p>
                </div>
                <div class="bg-white rounded-lg p-4 border border-blue-100">
                  <h5 class="font-semibold text-blue-800 mb-2">Detailed Analysis:</h5>
                  <p class="text-gray-700 text-base leading-relaxed">{{ selectedAsset?.explanation }}</p>
                </div>
                <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                  <h5 class="font-semibold text-yellow-800 mb-2">What This Means for Your Money:</h5>
                  <p class="text-yellow-700 text-base leading-relaxed">{{ selectedAsset?.what_it_means }}</p>
                </div>
              </div>
            </div>

            <!-- Market Prediction & Targets -->
            <div class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-6 border border-green-200">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-green-600 rounded-full flex items-center justify-center">
                  <span class="text-white text-lg">📈</span>
                </div>
                <h4 class="text-xl font-bold text-gray-900">Price Prediction & Targets</h4>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-white rounded-lg p-4 border border-green-100">
                  <h5 class="font-semibold text-green-800 mb-2">AI Forecast:</h5>
                  <p class="text-gray-700 text-base leading-relaxed mb-3">{{ selectedAsset?.market_prediction }}</p>
                  <div class="flex justify-between items-center">
                    <span class="text-sm text-gray-600">Next Target:</span>
                    <span class="font-bold text-green-600">{{ selectedAsset?.next_target }}</span>
                  </div>
                </div>
                <div class="bg-white rounded-lg p-4 border border-green-100">
                  <h5 class="font-semibold text-green-800 mb-2">Key Catalyst:</h5>
                  <p class="text-gray-700 text-base leading-relaxed mb-3">{{ selectedAsset?.catalyst || 'Market dynamics and technical factors' }}</p>
                  <div class="flex justify-between items-center">
                    <span class="text-sm text-gray-600">Confidence:</span>
                    <span class="font-bold text-green-600">{{ selectedAsset?.confidence?.toUpperCase() }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Price Chart Placeholder -->
          <div class="bg-white rounded-xl border border-gray-200 p-6">
            <div class="flex items-center justify-between mb-4">
              <h4 class="text-lg font-semibold text-gray-900">Price Chart</h4>
              <div class="flex gap-2">
                <button class="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded-lg font-medium">1D</button>
                <button class="px-3 py-1 text-xs bg-gray-100 text-gray-600 rounded-lg">1W</button>
                <button class="px-3 py-1 text-xs bg-gray-100 text-gray-600 rounded-lg">1M</button>
              </div>
            </div>
            
            <!-- Simple Chart Visualization -->
            <div class="bg-gray-50 rounded-lg p-8 text-center">
              <div class="w-full h-40 bg-gradient-to-r from-blue-100 via-blue-200 to-purple-100 rounded-lg flex items-center justify-center mb-4">
                <div class="text-center">
                  <div class="text-4xl mb-2">📈</div>
                  <div class="text-sm text-gray-600">Interactive Chart Coming Soon</div>
                  <div class="text-xs text-gray-500 mt-1">Real-time price data visualization</div>
                </div>
              </div>
              <div class="grid grid-cols-3 gap-4 text-sm">
                <div>
                  <div class="text-gray-500">Support</div>
                  <div class="font-medium">{{ selectedAsset?.next_target?.split('-')[0] || 'TBD' }}</div>
                </div>
                <div>
                  <div class="text-gray-500">Current</div>
                  <div class="font-medium">{{ selectedAsset?.current_move }}</div>
                </div>
                <div>
                  <div class="text-gray-500">Resistance</div>
                  <div class="font-medium">{{ selectedAsset?.next_target?.split('-')[1] || 'TBD' }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'

export default {
  name: 'SimpleSignalAI',
  setup() {
    const loading = ref(false)
    const sidebarOpen = ref(false)
    const activeCategory = ref('forex')
    const allAssets = ref([])
    const lastUpdate = ref('Loading...')
    const marketSummary = ref('Mixed market conditions with selective opportunities')
    const topStory = ref('Market participants watching for economic data releases')
    const historicalData = ref([])
    const selectedHistoricalDay = ref(null)
    const selectedHistoricalData = ref(null)
    const isViewingHistorical = ref(false)
    const currentData = ref(null)
    const selectedAsset = ref(null)
    const showAssetDetails = ref(false)
    const detailedAnalysis = ref(null)
    const loadingDetails = ref(false)
    const currentTime = ref('')
    const currentReports = ref([])
    const showPricing = ref(false)
    
    // Email subscription state
    const subscriptionEmail = ref('')
    const subscriptionLoading = ref(false)
    const subscriptionMessage = ref('')
    const subscriptionSuccess = ref(false)
    const showReportsSidebar = ref(false)
    const isSubscribing = ref(false)

    // Asset categories (Forex first - people like forex!)
    const assetCategories = ref([
      { id: 'forex', name: 'Forex', icon: '💱', count: 0 },
      { id: 'stocks', name: 'Stocks', icon: '📈', count: 0 },
      { id: 'crypto', name: 'Crypto', icon: '₿', count: 0 },
      { id: 'commodities', name: 'Commodities', icon: '🏅', count: 0 }
    ])

    // Market prediction (AI generated - no hardcoding!)
    const marketPrediction = ref({
      direction: 'Loading...',
      target: 'Analyzing...',
      confidence: 0,
      reasoning: 'AI is analyzing current market conditions...'
    })

    // Computed filtered assets
    const filteredAssets = computed(() => {
      if (activeCategory.value === 'all') return allAssets.value
      
      // Map category IDs to asset types
      const categoryMap = {
        'stocks': 'stock',
        'forex': 'forex', 
        'crypto': 'crypto',
        'commodities': 'commodity'
      }
      
      const targetType = categoryMap[activeCategory.value]
      return allAssets.value.filter(asset => asset.asset_type === targetType)
    })

    const getCategoryName = (categoryId) => {
      const category = assetCategories.value.find(cat => cat.id === categoryId)
      return category ? category.name : 'Assets'
    }

    const getAssetDescription = (asset) => {
      const descriptions = {
        'AAPL': 'Apple Inc. - Technology',
        'TSLA': 'Tesla Inc. - Electric Vehicles',
        'NVDA': 'NVIDIA - Semiconductors',
        'MSFT': 'Microsoft - Technology',
        'EUR/USD': 'Euro vs US Dollar',
        'GBP/USD': 'British Pound vs US Dollar',
        'BTC': 'Bitcoin - Cryptocurrency',
        'ETH': 'Ethereum - Cryptocurrency'
      }
      return descriptions[asset.symbol] || asset.asset_type.charAt(0).toUpperCase() + asset.asset_type.slice(1)
    }

    const getAssetIcon = (assetType) => {
      const icons = {
        'stock': '📈',
        'forex': '💱', 
        'crypto': '₿',
        'commodity': '🏅'
      }
      return icons[assetType] || '📊'
    }

    const getAssetCardStyle = (assetType) => {
      const styles = {
        'stock': 'bg-white border-blue-200 hover:border-blue-300',
        'forex': 'bg-green-50 border-green-200 hover:border-green-300',
        'crypto': 'bg-orange-50 border-orange-200 hover:border-orange-300',
        'commodity': 'bg-yellow-50 border-yellow-200 hover:border-yellow-300'
      }
      return styles[assetType] || 'bg-white border-gray-200'
    }

    const getMoveColor = (move) => {
      if (move.includes('up') || move.includes('+')) return 'text-green-600'
      if (move.includes('down') || move.includes('-')) return 'text-red-600'
      return 'text-gray-600'
    }

    const getActionStyle = (action) => {
      switch(action.toLowerCase()) {
        case 'buy': return 'bg-green-100 text-green-700 border border-green-200'
        case 'sell': return 'bg-red-100 text-red-700 border border-red-200'
        case 'watch': return 'bg-blue-100 text-blue-700 border border-blue-200'
        case 'hold': return 'bg-amber-100 text-amber-700 border border-amber-200'
        default: return 'bg-gray-100 text-gray-700 border border-gray-200'
      }
    }

    const getRiskStyle = (risk) => {
      switch(risk?.toLowerCase()) {
        case 'low': return 'bg-green-100 text-green-700'
        case 'medium': return 'bg-amber-100 text-amber-700'
        case 'high': return 'bg-red-100 text-red-700'
        default: return 'bg-gray-100 text-gray-700'
      }
    }

    const getActionBoxStyle = (action) => {
      switch(action?.toLowerCase()) {
        case 'buy': return 'bg-green-500 text-white border-green-400'
        case 'sell': return 'bg-red-500 text-white border-red-400'
        case 'watch': return 'bg-blue-500 text-white border-blue-400'
        case 'hold': return 'bg-amber-500 text-white border-amber-400'
        default: return 'bg-gray-500 text-white border-gray-400'
      }
    }

    const extractPrice = (priceText) => {
      if (!priceText) return null
      // Extract price patterns like $123.45, €1.23, 123.45, etc.
      const patterns = [
        /\$(\d+\.?\d*)/,  // $123.45
        /€(\d+\.?\d*)/,   // €1.23
        /(\d+\.\d+)/,     // 123.45
        /(\d+)/           // 123
      ]
      
      for (const pattern of patterns) {
        const match = priceText.toString().match(pattern)
        if (match) {
          const price = parseFloat(match[1])
          if (priceText.toString().includes('$') || price > 10) {
            return `$${price.toFixed(2)}`
          } else {
            return `$${price.toFixed(4)}`
          }
        }
      }
      return priceText
    }

    const getIconStyle = (assetType) => {
      const styles = {
        'stock': 'bg-blue-100 text-blue-600',
        'forex': 'bg-green-100 text-green-600', 
        'crypto': 'bg-orange-100 text-orange-600',
        'commodity': 'bg-yellow-100 text-yellow-600'
      }
      return styles[assetType] || 'bg-gray-100 text-gray-600'
    }

    const formatDate = (dateStr) => {
      const date = new Date(dateStr)
      const today = new Date()
      const yesterday = new Date(today)
      yesterday.setDate(yesterday.getDate() - 1)
      
      if (date.toDateString() === today.toDateString()) return 'Today'
      if (date.toDateString() === yesterday.toDateString()) return 'Yesterday'
      
      return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
    }

    const loadHistoricalData = async () => {
      const historical = []
      const today = new Date()
      
      // Try to load historical data (skip i=0 which is today, use "Live" instead)
      for (let i = 1; i <= 4; i++) {
        const date = new Date(today)
        date.setDate(date.getDate() - i)
        const dateStr = date.toISOString().split('T')[0]
        
        try {
          // Use new historical data path structure
          const response = await fetch(`/data/historical/${dateStr}/market_insights.json`)
          if (response.ok) {
            const data = await response.json()
            if (data.summary) {
              historical.push({
                date: dateStr,
                displayDate: i === 1 ? 'Yesterday' : i === 2 ? '2 days ago' : i === 3 ? '3 days ago' : `${i} days ago`,
                market_direction: data.summary.market_direction || 'Mixed',
                total_assets: data.summary.total_assets || 0,
                opportunity_score: data.summary.opportunity_score || data.market_prediction?.opportunity_score || 0,
                confidence: data.market_prediction?.confidence || 0,
                key_catalyst: data.summary.key_catalyst || 'Market analysis',
                available: true
              })
            }
          }
        } catch (error) {
        }
      }
      
      historicalData.value = historical // Keep chronological order (today first)
    }

    const viewHistoricalDay = async (day) => {
      selectedHistoricalDay.value = day
      isViewingHistorical.value = true
      
      try {
        const response = await fetch(`/data/historical/${day.date}/market_insights.json`)
        if (response.ok) {
          const historicalData = await response.json()
          selectedHistoricalData.value = historicalData
          
          // Replace current dashboard data with historical data
          if (historicalData.detailed_analyses) {
            const assets = []
            Object.values(historicalData.detailed_analyses).forEach(category => {
              if (category.analyses) {
                assets.push(...category.analyses)
              }
            })
            allAssets.value = assets
          }
          
          // Update market prediction
          if (historicalData.market_prediction) {
            marketPrediction.value = {
              direction: historicalData.market_prediction.direction,
              target: historicalData.market_prediction.target,
              confidence: historicalData.market_prediction.confidence,
              reasoning: historicalData.market_prediction.reasoning
            }
          }
          
          // Update market summary
          if (historicalData.market_discovery) {
            marketSummary.value = historicalData.market_discovery.market_summary
            topStory.value = historicalData.market_discovery.top_story
          }
          
          // Update category counts
          const categoryMap = {
            'stocks': 'stock',
            'forex': 'forex', 
            'crypto': 'crypto',
            'commodities': 'commodity'
          }
          
          assetCategories.value.forEach(category => {
            const targetType = categoryMap[category.id]
            category.count = assets.filter(asset => asset.asset_type === targetType).length
          })
          
          // Update last update time
          lastUpdate.value = `Historical data from ${formatDate(day.date)}`
        }
      } catch (error) {
        console.error('Failed to load historical data:', error)
      }
    }

    const backToToday = () => {
      selectedHistoricalDay.value = null
      selectedHistoricalData.value = null
      isViewingHistorical.value = false
      
      // Restore current data
      if (currentData.value) {
        const data = currentData.value
        
        // Restore assets
        if (data.detailed_analyses) {
          const assets = []
          Object.values(data.detailed_analyses).forEach(category => {
            if (category.analyses) {
              assets.push(...category.analyses)
            }
          })
          allAssets.value = assets
        }
        
        // Restore market prediction
        if (data.market_prediction) {
          marketPrediction.value = {
            direction: data.market_prediction.direction,
            target: data.market_prediction.target,
            confidence: data.market_prediction.confidence,
            reasoning: data.market_prediction.reasoning
          }
        }
        
        // Restore market summary
        if (data.market_discovery) {
          marketSummary.value = data.market_discovery.market_summary
          topStory.value = data.market_discovery.top_story
        }
        
        // Restore category counts
        const categoryMap = {
          'stocks': 'stock',
          'forex': 'forex', 
          'crypto': 'crypto',
          'commodities': 'commodity'
        }
        
        const assets = allAssets.value
        assetCategories.value.forEach(category => {
          const targetType = categoryMap[category.id]
          category.count = assets.filter(asset => asset.asset_type === targetType).length
        })
        
        lastUpdate.value = new Date().toLocaleString()
      }
    }

    const getDirectionColor = (direction) => {
      switch(direction?.toLowerCase()) {
        case 'bullish': return 'text-green-600'
        case 'bearish': return 'text-red-600'
        case 'sideways': return 'text-gray-600'
        case 'volatile': return 'text-purple-600'
        default: return 'text-gray-600'
      }
    }

    const getScoreColor = (score) => {
      if (score >= 80) return 'text-green-600'
      if (score >= 60) return 'text-yellow-600'
      if (score >= 40) return 'text-orange-600'
      return 'text-red-600'
    }

    const getAssetCount = (data, category) => {
      if (!data?.detailed_analyses) return 0
      return data.detailed_analyses[category]?.count || 0
    }

    const getTopAssets = (data) => {
      if (!data?.detailed_analyses) return []
      
      const allAssets = []
      Object.values(data.detailed_analyses).forEach(category => {
        if (category.analyses) {
          allAssets.push(...category.analyses)
        }
      })
      
      return allAssets.sort((a, b) => {
        // Sort by move magnitude (extract percentage)
        const getPercentage = (move) => {
          const match = move?.match(/([\d.]+)%/)
          return match ? parseFloat(match[1]) : 0
        }
        return getPercentage(b.current_move) - getPercentage(a.current_move)
      })
    }

    const getTodaysTrend = () => {
      const assets = filteredAssets.value
      if (assets.length === 0) return "Analyzing market trends..."
      
      const positiveCount = getPositiveCount()
      const negativeCount = getNegativeCount()
      const total = assets.length
      
      const positiveRatio = (positiveCount / total) * 100
      
      if (positiveRatio > 60) {
        return "Strong bullish momentum with broad-based buying interest. Multiple sectors showing strength."
      } else if (positiveRatio > 40) {
        return "Mixed sentiment with selective opportunities. Focus on quality names with strong catalysts."
      } else {
        return "Cautious market tone with defensive positioning. Risk management is key."
      }
    }

    const getWeeklyPrediction = () => {
      if (!marketPrediction.value || marketPrediction.value.direction === 'Loading...') {
        return "Generating weekly outlook based on current market conditions..."
      }
      
      const direction = marketPrediction.value.direction
      const confidence = marketPrediction.value.confidence
      
      if (direction === 'Bullish' && confidence > 70) {
        return "Expect continued upward momentum. Key sectors likely to outperform with earnings tailwinds."
      } else if (direction === 'Bearish' && confidence > 70) {
        return "Defensive positioning recommended. Watch for oversold bounce opportunities."
      } else if (direction === 'Volatile') {
        return "Range-bound trading expected. Focus on swing trading opportunities and volatility plays."
      } else {
        return "Consolidation phase likely. Wait for clearer directional signals before major positioning."
      }
    }

    const getTopMovers = () => {
      const assets = filteredAssets.value
      if (assets.length === 0) return ['Analyzing...']
      
      const sorted = assets.sort((a, b) => {
        const getPercentage = (move) => {
          const match = move?.match(/([\d.]+)%/)
          return match ? parseFloat(match[1]) : 0
        }
        return getPercentage(b.current_move) - getPercentage(a.current_move)
      })
      
      return sorted.slice(0, 3).map(asset => asset.symbol)
    }

    const getPositiveCount = () => {
      return filteredAssets.value.filter(asset => 
        asset.current_move && (asset.current_move.includes('up') || asset.current_move.includes('+'))
      ).length
    }

    const getNegativeCount = () => {
      return filteredAssets.value.filter(asset => 
        asset.current_move && (asset.current_move.includes('down') || asset.current_move.includes('-'))
      ).length
    }

    const viewAssetDetails = async (asset) => {
      selectedAsset.value = asset
      showAssetDetails.value = true
      loadingDetails.value = true
      detailedAnalysis.value = null
      
      try {
        let allDetailedData = null
        
        // If viewing historical data, try to load historical detailed analysis
        if (isViewingHistorical.value && selectedHistoricalDay.value) {
          ('📅 Loading historical detailed analysis for:', selectedHistoricalDay.value.date)
          const historicalResponse = await fetch(`/data/historical/${selectedHistoricalDay.value.date}/detailed_analyses.json`)
          if (historicalResponse.ok) {
            const historicalData = await historicalResponse.json()
            // Historical detailed_analyses.json is structured as {SYMBOL: analysis}
            allDetailedData = historicalData
            ('✅ Found historical detailed analysis for:', selectedHistoricalDay.value.date)
          }
        }
        
        // If no historical data found or viewing current data, use current detailed analysis
        if (!allDetailedData) {
          const response = await fetch('/data/detailed_analyses.json')
          if (response.ok) {
            allDetailedData = await response.json()
            ('✅ Using current detailed analysis')
          } else {
            throw new Error('Detailed analyses file not found')
          }
        }
        
        if (allDetailedData) {
          // Try multiple symbol formats to find the data
          let assetData = null
          const searchSymbol = asset.symbol.toUpperCase()
          
          // Check all keys to find the matching one (improved matching)
          for (const key of Object.keys(allDetailedData)) {
            const keyUpper = key.toUpperCase()
            // Try different matching strategies
            if (keyUpper.includes(searchSymbol) || 
                keyUpper.includes(searchSymbol.split(' ')[0]) ||
                keyUpper.includes(searchSymbol.split('(')[0].trim()) ||
                searchSymbol.includes(key.split(' ')[0].toUpperCase()) ||
                allDetailedData[key].symbol?.toUpperCase().includes(searchSymbol)) {
              assetData = allDetailedData[key]
              ('✅ Found detailed analysis using key:', key, 'for asset:', asset.symbol)
              break
            }
          }
          
          // If no match found, try exact symbol match in the data values
          if (!assetData) {
            for (const [key, data] of Object.entries(allDetailedData)) {
              if (data.symbol && data.symbol.toUpperCase().includes(searchSymbol)) {
                assetData = data
                ('✅ Found detailed analysis by symbol value:', data.symbol, 'for asset:', asset.symbol)
                break
              }
            }
          }
          
          if (assetData) {
            detailedAnalysis.value = assetData
          } else {
            throw new Error(`No detailed analysis found for ${asset.symbol}`)
          }
        }
      } catch (error) {
        console.error('Failed to load AI analysis:', error)
        ('⚠️ AI analysis not available for:', asset.symbol)
        ('💡 Run "python agents.py" to generate detailed analysis')
        // Show error message instead of mock data
        detailedAnalysis.value = {
          error: true,
          message: 'Detailed analysis not available',
          suggestion: 'Run AI analysis to generate detailed insights',
          symbol: asset.symbol,
          asset_type: asset.asset_type
        }
      }
      
      loadingDetails.value = false
    }

    const closeAssetDetails = () => {
      selectedAsset.value = null
      showAssetDetails.value = false
      detailedAnalysis.value = null
      loadingDetails.value = false
    }
    
    const generateMockDetailedAnalysis = (asset) => {
      // Generate realistic mock data based on asset type
      const basePrice = Math.random() * 1000 + 50
      const priceHistory = []
      let currentPrice = basePrice
      
      for (let i = 0; i < 7; i++) {
        const change = (Math.random() - 0.5) * 10
        currentPrice += change
        priceHistory.push({
          time: `${9 + i}:00`,
          price: Math.round(currentPrice * 100) / 100,
          volume: Math.floor(Math.random() * 2000) + 500
        })
      }
      
      const priceChanges = {
        "24h": `${Math.random() > 0.5 ? '+' : '-'}${(Math.random() * 5).toFixed(1)}%`,
        "7d": `${Math.random() > 0.5 ? '+' : '-'}${(Math.random() * 15).toFixed(1)}%`,
        "30d": `${Math.random() > 0.5 ? '+' : '-'}${(Math.random() * 30).toFixed(1)}%`
      }
      
      return {
        symbol: asset.symbol,
        asset_type: asset.asset_type,
        current_price: `$${currentPrice.toFixed(2)}`,
        price_change_24h: priceChanges["24h"],
        price_change_7d: priceChanges["7d"],
        price_change_30d: priceChanges["30d"],
        volume_24h: `${(Math.random() * 10 + 1).toFixed(1)}M`,
        market_cap: asset.asset_type === 'stock' ? `$${(Math.random() * 500 + 50).toFixed(1)}B` : 'N/A',
        
        technical_indicators: {
          rsi: Math.floor(Math.random() * 30) + 45,
          macd: ['bullish', 'bearish', 'neutral'][Math.floor(Math.random() * 3)],
          moving_averages: {
            sma_20: ['above', 'below', 'at'][Math.floor(Math.random() * 3)],
            sma_50: ['above', 'below', 'at'][Math.floor(Math.random() * 3)],
            sma_200: ['above', 'below', 'at'][Math.floor(Math.random() * 3)]
          },
          support_levels: ['$95.50', '$92.30', '$89.10'],
          resistance_levels: ['$108.75', '$112.40', '$115.80'],
          trend: ['bullish', 'bearish', 'sideways'][Math.floor(Math.random() * 3)]
        },
        
        price_history: priceHistory,
        
        trading_signals: {
          primary_signal: ['BUY', 'SELL', 'HOLD', 'WATCH'][Math.floor(Math.random() * 4)],
          signal_strength: ['Strong', 'Moderate', 'Weak'][Math.floor(Math.random() * 3)],
          entry_price: 'Current levels',
          stop_loss: '5% below entry',
          take_profit: '12% above entry',
          risk_reward_ratio: '1:2.4',
          time_horizon: ['Short-term', 'Medium-term', 'Long-term'][Math.floor(Math.random() * 3)]
        },
        
        risk_metrics: {
          volatility: ['High', 'Medium', 'Low'][Math.floor(Math.random() * 3)],
          beta: asset.asset_type === 'stock' ? (Math.random() * 2 + 0.5).toFixed(1) : 'N/A',
          correlation_with_market: ['High', 'Medium', 'Low'][Math.floor(Math.random() * 3)],
          liquidity: 'High',
          risk_score: Math.floor(Math.random() * 5) + 4
        },
        
        news_sentiment: {
          overall_sentiment: ['Positive', 'Negative', 'Neutral'][Math.floor(Math.random() * 3)],
          sentiment_score: (Math.random() * 0.6 + 0.2).toFixed(1),
          key_news_factors: ['Earnings beat', 'Sector rotation', 'Market volatility'],
          social_media_buzz: ['High', 'Medium', 'Low'][Math.floor(Math.random() * 3)]
        },
        
        detailed_explanation: `Advanced analysis shows ${asset.symbol} exhibiting ${['strong', 'moderate', 'mixed'][Math.floor(Math.random() * 3)]} technical signals with ${['positive', 'neutral', 'cautious'][Math.floor(Math.random() * 3)]} fundamental outlook. Market conditions suggest ${['continued momentum', 'consolidation phase', 'potential reversal'][Math.floor(Math.random() * 3)]} in the near term.`,
        
        trading_recommendation: 'Consider position sizing based on risk tolerance and market conditions',
        key_levels_to_watch: 'Monitor key technical levels for breakout or breakdown signals',
        
        scenario_analysis: {
          bullish_case: 'Strong fundamentals and technical breakout could drive significant gains',
          bearish_case: 'Market headwinds or sector weakness could pressure prices lower',
          base_case: 'Gradual price appreciation with normal market volatility expected'
        },
        
        generated_at: new Date().toISOString()
      }
    }

    const subscribeToReports = async () => {
      if (!subscriptionEmail.value) {
        subscriptionMessage.value = 'Please enter your email address'
        subscriptionSuccess.value = false
        return
      }

      subscriptionLoading.value = true
      subscriptionMessage.value = ''

      try {
        // Load existing subscribers from JSON
        let subscribers = []
        try {
          const response = await fetch('/data/subscribers.json')
          if (response.ok) {
            subscribers = await response.json()
          }
        } catch (e) {
          ('No existing subscribers file')
        }

        // Check if email already exists
        if (subscribers.find(s => s.email === subscriptionEmail.value)) {
          subscriptionMessage.value = 'Email already subscribed!'
          subscriptionSuccess.value = false
          subscriptionLoading.value = false
          return
        }

        // Add new subscriber
        const newSubscriber = {
          email: subscriptionEmail.value,
          subscribed_at: new Date().toISOString(),
          active: true,
          id: Date.now() // Simple ID generation
        }

        subscribers.push(newSubscriber)

        // Save to localStorage and trigger download of updated subscribers
        localStorage.setItem('signalai_subscribers', JSON.stringify(subscribers))
        
        // Create and download updated subscribers JSON file
        const blob = new Blob([JSON.stringify(subscribers, null, 2)], { type: 'application/json' })
        const url = URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = `subscribers_${new Date().toISOString().split('T')[0]}.json`
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
        URL.revokeObjectURL(url)

        subscriptionMessage.value = '✅ Successfully subscribed! Subscriber data downloaded.'
        subscriptionSuccess.value = true
        subscriptionEmail.value = ''
        
      } catch (error) {
        console.error('Subscription error:', error)
        subscriptionMessage.value = 'Subscription successful! Email saved locally.'
        subscriptionSuccess.value = true
        subscriptionEmail.value = ''
      } finally {
        subscriptionLoading.value = false
      }
    }

    const subscribeEmail = async () => {
      if (!subscriptionEmail.value) {
        subscriptionMessage.value = 'Please enter your email address'
        subscriptionSuccess.value = false
        return
      }

      isSubscribing.value = true
      subscriptionMessage.value = ''

      try {
        // Trigger GitHub Actions workflow to update subscribers.json
        const response = await fetch('https://api.github.com/repos/gradan-hash/SIGNALAI/dispatches', {
          method: 'POST',
          headers: {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'Bearer ghp_YOUR_GITHUB_TOKEN_HERE', // You'll need to replace this
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            event_type: 'new_subscription',
            client_payload: {
              email: subscriptionEmail.value,
              timestamp: new Date().toISOString()
            }
          })
        })

        if (response.ok) {
          subscriptionMessage.value = '✅ Successfully subscribed! You will receive daily PDF reports.'
          subscriptionSuccess.value = true
          subscriptionEmail.value = ''
        } else {
          throw new Error(`GitHub API error: ${response.status}`)
        }
        
      } catch (error) {
        console.error('Subscription error:', error)
        // Fallback to localStorage as backup
        const subscribers = JSON.parse(localStorage.getItem('signalai_subscribers') || '[]')
        
        const newSubscriber = {
          email: subscriptionEmail.value,
          subscribed_at: new Date().toISOString(),
          active: true,
          id: Date.now()
        }
        
        subscribers.push(newSubscriber)
        localStorage.setItem('signalai_subscribers', JSON.stringify(subscribers))
        
        subscriptionMessage.value = '✅ Subscribed! Please set up GitHub token for automatic processing.'
        subscriptionSuccess.value = true
        subscriptionEmail.value = ''
      } finally {
        isSubscribing.value = false
      }
    }

    const loadData = async () => {
      loading.value = true
      try {
        // Try to load market insights from search agent
        const response = await fetch('/data/market_insights.json')
        if (response.ok) {
          const data = await response.json()
          
          // Store current data for restoration
          currentData.value = data
          
          // Flatten all analyses into single array
          const assets = []
          if (data.detailed_analyses) {
            Object.values(data.detailed_analyses).forEach(category => {
              if (category.analyses) {
                assets.push(...category.analyses)
              }
            })
          }
          
          allAssets.value = assets
          
          // Update market summary and AI prediction
          if (data.market_discovery) {
            marketSummary.value = data.market_discovery.market_summary || marketSummary.value
            topStory.value = data.market_discovery.top_story || topStory.value
          }
          
          // Update AI-generated market prediction
          if (data.market_prediction) {
            marketPrediction.value = {
              direction: data.market_prediction.direction,
              target: data.market_prediction.target,
              confidence: data.market_prediction.confidence,
              reasoning: data.market_prediction.reasoning
            }
          }

          // Load historical data if available
          if (data.historical_comparison) {
            historicalData.value = data.historical_comparison.slice(-7) // Last 7 days
          } else {
            // Try to load historical data from individual files
            loadHistoricalData()
          }
          
          // Update category counts with correct mapping
          const categoryMap = {
            'stocks': 'stock',
            'forex': 'forex', 
            'crypto': 'crypto',
            'commodities': 'commodity'
          }
          
          assetCategories.value.forEach(category => {
            const targetType = categoryMap[category.id]
            category.count = assets.filter(asset => 
              asset.asset_type === targetType
            ).length
          })
          
          lastUpdate.value = new Date().toLocaleTimeString()
        }
      } catch (error) {
        console.error('Failed to load data:', error)
        // Demo data
        allAssets.value = [
          {
            symbol: 'AAPL',
            asset_type: 'stock',
            current_move: 'up 1.2%',
            why_simple: 'Apple released better-than-expected iPhone sales numbers',
            explanation: 'Apple just reported quarterly earnings that beat Wall Street expectations.',
            what_it_means: 'This is generally good news for Apple investors.',
            action: 'buy',
            confidence: 'high',
            risk: 'low',
            next_target: '$185-190',
            market_prediction: 'Continued strength expected in tech sector'
          }
        ]
        lastUpdate.value = new Date().toLocaleTimeString()
      }
      loading.value = false
    }

    const previewReport = (report) => {
      // Open PDF in new window for preview
      window.open(report.pdf_url, '_blank')
    }

    const loadCurrentReports = async () => {
      try {
        const response = await fetch('/data/current_reports.json')
        if (response.ok) {
          const data = await response.json()
          currentReports.value = data.current_reports || []
          ('✅ Current reports loaded:', currentReports.value.length)
        }
      } catch (error) {
        ('Current reports not available')
      }
    }

    onMounted(() => {
      loadData()
      loadCurrentReports()
      // Refresh every 15 minutes
      setInterval(loadData, 15 * 60 * 1000)
      
      // Update current time every second
      const updateTime = () => {
        currentTime.value = new Date().toLocaleTimeString('en-US', { 
          hour12: false,
          hour: '2-digit', 
          minute: '2-digit', 
          second: '2-digit' 
        })
      }
      updateTime() // Set initial time
      setInterval(updateTime, 1000) // Update every second
    })

    return {
      loading,
      sidebarOpen,
      activeCategory,
      assetCategories,
      marketPrediction,
      marketSummary,
      topStory,
      lastUpdate,
      currentTime,
      currentReports,
      showPricing,
      showReportsSidebar,
      previewReport,
      filteredAssets,
      historicalData,
      selectedHistoricalDay,
      selectedHistoricalData,
      isViewingHistorical,
      selectedAsset,
      showAssetDetails,
      detailedAnalysis,
      loadingDetails,
      getCategoryName,
      getAssetDescription,
      getAssetIcon,
      getAssetCardStyle,
      getIconStyle,
      getMoveColor,
      getActionStyle,
      getActionBoxStyle,
      getRiskStyle,
      extractPrice,
      formatDate,
      viewHistoricalDay,
      backToToday,
      getDirectionColor,
      getScoreColor,
      getAssetCount,
      getTopAssets,
      getPositiveCount,
      getNegativeCount,
      getTodaysTrend,
      getWeeklyPrediction,
      getTopMovers,
      viewAssetDetails,
      closeAssetDetails,
      generateMockDetailedAnalysis,
      loadData,
      subscriptionEmail,
      subscriptionLoading,
      subscriptionMessage,
      subscriptionSuccess,
      isSubscribing,
      subscribeToReports,
      subscribeEmail
    }
  }
}
</script>

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
}
</style>