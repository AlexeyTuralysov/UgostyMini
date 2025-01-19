

export default function getStaffFromJwt(jwt) {
    try {
        const decodedToken = JSON.parse(atob(jwt.split(".")[1]));
        const isStaff = decodedToken.is_admin_user;

        return isStaff;
        
    }
    catch(e) {
        console.error("ВЫ НЕ АДМИН!",e);
        return null;

    }
}
