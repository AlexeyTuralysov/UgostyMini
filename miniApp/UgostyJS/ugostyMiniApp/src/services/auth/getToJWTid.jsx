

export default function getToJWTid(jwt) {
    try {
        const decodedToken = JSON.parse(atob(jwt.split(".")[1]));
        const currentId = decodedToken.user_id;
        return currentId;
    }
    catch(e) {
        console.error("Error in getToJWTid:", e);
        return null;

    }
}
