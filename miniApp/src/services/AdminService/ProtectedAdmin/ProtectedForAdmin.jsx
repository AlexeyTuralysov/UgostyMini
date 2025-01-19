
import getStaffFromJwt from "./getStaffFromJwt"
import { Navigate } from "react-router-dom";

export default function ProtectedForAdmin({ children }) {
    const jwt = localStorage.getItem('token');
    const isStaff = getStaffFromJwt(jwt);

    if (isStaff !== true){
        console.log("рендер");
        return <Navigate to="/" />;
    }

    return children

}
