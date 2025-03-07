import React, {createContext, useContext, useState} from "react";

export const AuthContext = createContext(null);

export function useAuthContext() {
    const context = useContext(AuthContext)

    if (!context) {
        throw new Error("useAuthContext must be used within the AuthContextProvider")
    }

    return context
}

export function AuthContextProvider({children}) {

    const [isLoggedIn, setIsLoggedIn] = useState(false)

    const refreshAccessToken = async () => {
        return await fetch('http://127.0.0.1:8000/api/token/refresh', {
          method: 'POST',
          credentials: 'include', // Automatically include cookies (refresh token)
        })
        .then(response => {
            if (response.ok) {
                setIsLoggedIn(true)
                return response.status
            } else {
                setIsLoggedIn(false)
            }
        })
        .catch(err => {
            setIsLoggedIn(false)
            console.error('Error refreshing access token:', err);
            return null;
        });
      }
      
      const value = {refreshAccessToken}
      return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
      )
}