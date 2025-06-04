import { Routes, Route } from 'react-router-dom';
import Author from "./pages/Author/Author";
import { useEffect } from 'react';
import { useLaunchParams, isTMA, init, viewport } from "@telegram-apps/sdk-react";
import Home from "./pages/Home/Home";

function App() {

  const author = "root";

  //const launchParams = useLaunchParams();
  //const author = launchParams.startParam
  //const author = launchParams.startParam;

  useEffect(() => {
    async function initTg() {
      if (await isTMA()) {
        init();

        if (viewport.mount.isAvailable()) {
          await viewport.mount();
          viewport.expand();
        }

        if (viewport.requestFullscreen.isAvailable()) {
          await viewport.requestFullscreen();
        }
      }
    }
    initTg();

  }, []);


  return (
    <>
 
      <Routes>
           <Route path="/" element={<Author author={author} />} />
      </Routes>

     

{/*        
      <Routes>
        {author 
          ? <Route path="/" element={<Author author={author} />} />
          : <Route path="/" element={<Home />} /> 

        }
        
    
        
    
      </Routes>

     */}


      {/*
      <Routes>
        <Route element={<Header />}>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Auth />} />

          <Route path="/admin" element={
            <ProtectedForAdmin>
              <AdminPage />
            </ProtectedForAdmin>
          } />

          <Route path="/:author" element={<Author />} />

        </Route>

        <Route element={<HeaderManager />}>



          <Route
            path="/:author/edit"
            element={
              <ProtectedRoute>
                <EditProfile />
              </ProtectedRoute>
            }
          />

          <Route
            path="/:author/donations"
            element={
              <ProtectedRoute>
                <PayDonation />
              </ProtectedRoute>
            }
          />
        </Route>






      </Routes>
      */}
    </>
  )
}

export default App
