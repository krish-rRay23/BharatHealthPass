import axios from 'axios';

const api = axios.create({
    baseURL: '/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
});

export const identityApi = {
    login: (mobile: string, name: string) => api.post('/identity/login', { mobile, name }),
    grantConsent: (user_id: string, purpose: string) => api.post('/identity/consent', { user_id, purpose }),
    getKyc: (user_id: string) => api.get(`/identity/kyc/${user_id}`),
};

export default api;
