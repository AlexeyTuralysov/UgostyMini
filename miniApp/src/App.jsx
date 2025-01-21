import { Routes, Route } from 'react-router-dom';
import Author from "./pages/Author/Author";
import { useLaunchParams } from "@telegram-apps/sdk-react";
import Home from "./pages/Home/Home";

function App() {

  //const author = "alexey";

  const launchParams = useLaunchParams();
  const author = launchParams.startParam;
  //const author = launchParams.startParam;
  return (
    <>
     
      <Routes>
        
        <Route path="/:author" element={<Author author={author} />} />
        <Route path='/' element ={ <Home/> } />
      </Routes>
    

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
